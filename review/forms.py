from django import forms
from .models import Post
# 모듈 import방식 참조


class PostForm(forms.ModelForm):
    # 아 PostForm은 models모듈의 Post 클래스를 상속하는구나

    class Meta:
        model = Post
        fields = ('title', 'review', 'score', 'price',)
