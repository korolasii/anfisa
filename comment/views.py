from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm
from django.contrib import messages
# Create your views here.

def comment_list(request):
    template = 'comment/comment_list.html'
    comments = Comment.objects.all()
    # только то мороженое, у кторого есть флаг on_main
    return render(request, template, {'comments': comments})

def create(request):
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
               
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.save()
            messages.add_message(request, messages.INFO, 'Cтаття створенна')
            return redirect('comment_list')
    else:
        form = CommentForm()
    return render(request, 'comment/create_comment.html', {'form': form})