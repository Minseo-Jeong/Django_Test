from django.shortcuts import render, get_object_or_404
from polls.models import Question, Choice
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    latest_question_list = Question.objects.all().order_by('pub_date')[:5]
    return render(request,'polls/index.html',{'latest_question_list':latest_question_list})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})
    
