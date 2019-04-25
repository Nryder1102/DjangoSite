from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'index/index.html'
    def get_queryset(self):
        return render(request, 'index/index.html'),
