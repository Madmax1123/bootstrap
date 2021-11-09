from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .form import PostForm

def index(request):

    return render(request, 'index.html')

def post_new(request):
    form = PostForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        nota1 = request.POST.get('nota1')
        nota2 = request.POST.get('nota2')
        nota3 = request.POST.get('nota3')
        nota4 = request.POST.get('nota4')

        post.save()
        return HttpResponseRedirect('')
    else:
        form = PostForm()
    return  render(request, 'criar_boletim.html', {'form': form})
