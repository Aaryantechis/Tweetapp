from django import forms
from django.forms.fields import ImageField
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Tweets
from .form import PostForm

# Create your views here.


def index(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        img = PostForm(request.FILES)
        print(img)
        # If the form is valid
        if form.is_valid():
            # Yes, Save
            form.save()
            print("hello its valid")
            return HttpResponseRedirect("/")
        else:
            print("its not valid")
            return HttpResponse("not valid")
    tweets = Tweets.objects.all().order_by("-created_at")
    form = PostForm()
    return render(request, "index.html", {"tweets": tweets, "form": form})


def likes(request, id):
    likedtweet = Tweets.objects.get(id=id)
    likedtweet.like_count += 1
    likedtweet.save()
    return HttpResponseRedirect("/")


def delete(request, id):
    deletetweet = Tweets.objects.get(id=id)
    deletetweet.delete()
    return HttpResponseRedirect("/")


def edit(request, id):
    if request.method == "GET":
        edittweet = Tweets.objects.get(id=id)
        return render(request, "edit.html", {"edittweet": edittweet})
    if request.method == "POST":
        edittweet = Tweets.objects.get(id=id)
        form = PostForm(request.POST, request.FILES, instance=edittweet)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        else:
            return HttpResponse("not valid")
