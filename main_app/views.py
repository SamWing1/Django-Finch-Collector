from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch, Tag
from .forms import SightingForm


def home(request):
    return render(request, 'main_page1.html')

def about(request):
    return render(request, 'about.html')

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    id_list = finch.tags.all().values_list('id')
    tags_finch_doesnt_have = Tag.objects.exclude(id__in=id_list)
    sighting_form = SightingForm()
    return render(request, 'finches/detail.html', { 'finch' : finch, 'sighting_form' : sighting_form, 'tags' : tags_finch_doesnt_have })

def add_sighting(request, finch_id):
    form = SightingForm(request.POST)
    if form.is_valid():
        new_sighting = form.save(commit=False)
        new_sighting.finch_id = finch_id
        new_sighting.save()
    return redirect('detail', finch_id=finch_id)

def assoc_tag(request, finch_id, tag_id):
    Finch.objects.get(id=finch_id).tags.add(tag_id)
    return redirect('detail', finch_id=finch_id)

class FinchList(ListView):
    model = Finch
    template_name = 'finches/index.html'

class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'color', 'description', 'age']
    success_url = '/finches/'

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['color', 'description', 'age']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'

class TagList(ListView):
    model = Tag

class TagDetail(DetailView):
    model = Tag

class TagCreate(CreateView):
    model = Tag
    fields = '__all__'

class TagUpdate(UpdateView):
    model = Tag
    fields = ['color', 'tracking']

class TagDelete(DeleteView):
    model = Tag
    success_url = '/tags/'