from.models import Post,Category,Tag
from django import forms
from posts.models import Category , Tag

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image', 'title','content','rate','category','tags')




class SearchForm(forms.Form):
    search = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder":"поиск"}),
        )
    category = forms.ModelChoiceField(queryset=Category.objects.all(),required=False)
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple)
    orderings = {
        ('title','по загаловку'),
        ('-title','по заголовку(обратно)'),
        ('rate','по оценке'),
        ('-rate','по оценке (обратно)'),
        ('created_at','по дате создания'),
        ('-created_at','по дате создания (обратно)')
    }
    ordering = forms.ChoiceField(choices=orderings, widget=forms.Select(attrs=
        {"class":"form-control"}))