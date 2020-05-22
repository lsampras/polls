from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TODO
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'TODO/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        """Return the TODO's in latest to oldest fashion."""
        return TODO.objects.order_by('-date')


def new(request):
    return render(request, 'TODO/new.html')

def create(request):
    try:
        task_text = request.POST['task']
    except Exception as err:
        return HttpResponseRedirect(reverse('TODO:index'))

    else:
        todo = TODO(task=task_text,date=timezone.now())
        todo.save()
        return HttpResponseRedirect(reverse('TODO:index'))

def delete(request,todo_id):
    todo = TODO.objects.get(pk=todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('TODO:index'))

def update(request,todo_id):
    todo = TODO.objects.get(pk=todo_id)
    todo.done = not todo.done

    todo.save()
    return HttpResponseRedirect(reverse('TODO:index'))