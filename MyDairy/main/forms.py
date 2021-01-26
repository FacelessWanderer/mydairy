from django import forms
from .models import Post, Category, Comment
from django.forms import ModelForm


#choices = [('global', 'global'), ('city', 'city'), ('story', 'story'),]
"""choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)"""

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'category', 'body']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'elder', 'type': 'hidden'}),
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'without "#"'}), # .Select choices=choice_list,
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'type': 'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }