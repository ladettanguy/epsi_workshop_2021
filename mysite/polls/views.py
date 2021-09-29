import json
from .models import Question, Electeur
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.forms.models import model_to_dict
from django.utils import timezone
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, './detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        q = request.POST['id']
        dict_obj = {'mabite': q}
        serialized = json.dumps(dict_obj, cls=DjangoJSONEncoder)
        return HttpResponse(serialized, content_type='application/json')


def vote(request, question_id):
    return HttpResponse(question_id)


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, './index.html', context)


def newQuestion(request):
    q = Question(question_text=request.GET.get("texte", 'default'), pub_date=timezone.now())
    dict_obj = model_to_dict(q)
    serialized = json.dumps(dict_obj, cls=DjangoJSONEncoder)
    q.save()
    return HttpResponse(serialized)

def infoElecteur(request):
    electeur = Electeur(id_electeur=request.GET.get("id", 1), token=333333)
    electeur.save()
    return HttpResponse(333333)

