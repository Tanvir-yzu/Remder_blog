from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content']
        widgets = {
            'author': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-2xl',
                'placeholder': 'Your name'
            }),
            'content': forms.Textarea(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-2xl',
                'rows': 4,
                'placeholder': 'Write your comment here...'
            })
        }
