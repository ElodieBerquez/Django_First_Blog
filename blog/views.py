from django.shortcuts import render
from django.http import Http404


from.models import Post

def index(request):
     posts = Post.objects.all()
     return render(request, 'blog/index.html', {'posts': posts})

def show (request, id):
    try:
         post = Post.objects.get(pk=id)
    except Post.DoesNotExist:
        raise Http404 ("Désolée, le post #{} n'existe pas." .format(id))
        
    return render (request,'blog/show.html', {'post': post})
