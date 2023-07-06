import openai
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import User, Post

openai.api_key = 'AI_API_KEY'
AI_MODEL = 'gpt-3.5-turbo'
USER_ROLE = 'user'


def home(request):
    return render(request, 'login-signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('lowfoundai', username=user.username)
        messages.error(request, 'Invalid username or password3')
    return redirect('home')


def logout_view(request):
    logout(request)
    return redirect('home')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.create_user(username, password=password)
            login(request, user)
            return redirect('lowfoundai', username=username)
        except IntegrityError:
            messages.error(
                request, 'User with this username or password already exists')
            return render(request, 'login-signup.html')
    return redirect('home')


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
        response = openai.ChatCompletion.create(
            model=AI_MODEL,
            messages=[
                {"role": USER_ROLE, "content": question}
                ]
        )
        answer = response.choices[0].message
    except Exception as e:
        messages.error(request, str(e))
        return redirect('lowfoundai', username)
    Post.objects.create(
        author=request.user,
        question=question,
        answer=answer
    )
    return redirect('lowfoundai', username)
