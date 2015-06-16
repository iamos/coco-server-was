from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from posts.models import Post

@login_required
def index(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'dashboard/index.html', context)
