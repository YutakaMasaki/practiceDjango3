from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):

    content = forms.CharField(widget=forms.TextInput(attrs={"size":80}))

    class Meta:
        model = Blog
        fields = ["content", ]