from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import  Choice, Question 
from .models import Noticia 


class DetailView(generic.DetailView):
    model = Noticia
    template_name = 'postList.html'


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]





class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'   


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    ... # same as above, no changes needed.    