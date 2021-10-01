import hashlib
import json
from random import random

from django.core.exceptions import BadRequest

from .models import Electeur, Candidat, Block
from django.http import HttpResponse, Http404
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage
import requests


@csrf_exempt
def login(request):
    if request.method == 'POST':
        id_electeur = request.POST['id']
        password = request.POST['password']

        # appel de l'API
        r = requests.post('https://fake-fc.herokuapp.com/api/', data={'id': id_electeur, 'password': password})
        if r.status_code != 200:
            raise Http404()

        data = json.loads(r.content)

        if data['success']:
            user = data['user']
            # mail
            mail = user['email']

            # Génération du code a double identification
            token = random() * 65536
            token = hex(int(token))
            token = token[2::]

            email = EmailMessage('authentification', 'ton code: %s' % token, to=[mail])
            email.send()

            # création de l'electeur
            Qs = Electeur.objects.filter(id_electeur=user['id'])
            if len(Qs) == 1:
                electeur = Qs[0]
                electeur.token = token
            elif len(Qs) == 0:
                new_electeur = Electeur(id_electeur=user['id'], token=token)
                new_electeur.save()
            else:
                raise Exception()

            # Réponse
            dict_obj = {'token': user['id']}
            serialized = json.dumps(dict_obj, cls=DjangoJSONEncoder)
            return HttpResponse(serialized, content_type='application/json')
        else:
            raise Http404()


def auth(request):
    if request.method == 'POST':
        id_electeur = request.POST['token']
        token = request.POST['auth']
        Qs = Electeur.objects.filter(id_electeur=id_electeur)
        if len(Qs) == 1:
            electeur = Qs[0]
        else:
            raise Exception()
        if electeur.token == token:
            dict_obj = {'success': True}
            serialized = json.dumps(dict_obj, cls=DjangoJSONEncoder)
            return HttpResponse(serialized)
        else:
            return Http404()
    else:
        return Http404()


def getCandidat(request):
    listeCandidat = Candidat.objects.all()
    listeDictionnaire = []
    for c in listeCandidat:
        dict_obj = model_to_dict(c)
        listeDictionnaire.append(dict_obj)
    listeJson = json.dumps(listeDictionnaire)
    return HttpResponse(listeJson)


def getVote(request):
    if request.method == 'POST':
        id_electeur = request.POST['token']
        Qs = Electeur.objects.filter(id_electeur=id_electeur)
        if len(Qs) == 1:
            electeur = Qs[0]
        else:
            raise Exception()
        if electeur.a_vote:
            raise BadRequest()

        electeur.a_vote = True
        electeur.save()
        id_candidat = request.POST['candidat']
        addBlock(id_candidat)
        dict_obj = {'success': True}
        serialized = json.dumps(dict_obj, cls=DjangoJSONEncoder)
        return HttpResponse(serialized)


def addBlock(id):
    last_bloc_str = Block.objects.latest('id').actuel
    lastBlock = eval(last_bloc_str)
    hashPrecedent = hash(last_bloc_str)
    lastBlock[id] += 1

    my_dict_str = str(lastBlock)
    block = Block(hashPrecedent=hashPrecedent, actuel=my_dict_str)
    block.save()
