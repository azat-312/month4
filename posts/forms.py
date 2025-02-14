from.models import Post,Category,Tag
from django import forms

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image', 'title','content','rate','category','tags')
        