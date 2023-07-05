import os
import openai
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import check_password

from .models import User, Post

openai.api_key = os.getenv('AI_API_KEY ')
AI_MODEL = 'gpt-3.5-turbo'


def home(request):
    return render(request, 'login-signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = get_object_or_404(User, username=username)
        if user and check_password(password, user.password):
            login(request, user)
            return redirect('lowfoundai', username=user.username)
    return redirect('home')


def logout_view(request):
    logout(request)
    return redirect('home')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username, password=password)
        login(request, user)
        return redirect('lowfoundai', username=username)
    return render(request, 'home')


@login_required
def lowfound_ai_view(request, username):
    posts = Post.objects.filter(author=request.user)
    context = {
        'posts': posts,
        'username': username,
        'user': request.user
    }
    return render(request, 'lowfound-openai.html', context)


def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    username = request.user.username
    if request.user == post.author:
        post.delete()
    return redirect('lowfoundai', username)


def post_create(request):
    question = request.POST.get('question')
    username = request.user.username
    try:
        response = openai.Completion.create(
            model=AI_MODEL,
            prompt=question
        )
        answer = response.choices[0].text.strip()
    except Exception as e:
        answer = f"Error: {str(e)}"
    Post.objects.create(
        author=request.user,
        question=question,
        answer=answer
    )
    return redirect('lowfoundai', username)
