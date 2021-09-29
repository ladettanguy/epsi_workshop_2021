from django.http import HttpResponse,HttpRequest, Http404
from .models import Question
from django.shortcuts import render
from django.forms.models import model_to_dict
from django.template import loader
from django.utils import timezone
import json
from django.core.serializers.json import DjangoJSONEncoder

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, './detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

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

