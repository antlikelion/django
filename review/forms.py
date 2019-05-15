from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User
# 모듈 import방식 참조


class PostForm(forms.ModelForm):
    # 아 PostForm은 models모듈의 Post 클래스를 상속하는구나

    class Meta:
        model = Post
        fields = ('title', 'review', 'score', 'price',
                  'writer', 'publisher', 'img',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password',)
        labels = {'username': 'ID(E-mail)', }
        widgets = {'password': forms.PasswordInput(), }
