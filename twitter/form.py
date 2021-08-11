from django import forms
from django.db import models
from django import forms
from django.db.models import fields
from .models import Tweets
from cloudinary.forms import CloudinaryFileField


class PostForm(forms.ModelForm):
    class Meta:
        model = Tweets
        fields = ["name", "body", "image"]
