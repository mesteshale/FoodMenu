from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Group
# Create your views here.

class IndexClassView(ListView):
    model = Group;
    template_name = 'group/index.html'
    context_object_name = 'group_list'

class CreateGroup(CreateView):
    model = Group;
    template_name = 'group/create.html'
    fields = ['cate_name','cate_desc']

    def form_valid(self, form):
        return super().form_valid(form)
    