from django import forms
from .models import Post
from ckeditor_uploader.fields import RichTextUploadingField

class CreatePost(forms.ModelForm):
    class Meta:
        model = Post

        fields = ['title', 'tag', 'file', 'body'] 
        widgets = {
            'title': forms.TextInput(
                attrs={'style': 'width: 100%', 'placeholder': '제목을 입력하세요.'},
                label=''
            ),
            'tag': forms.Select(
                attrs={'style': 'placeholder': '태그를 입력하세요.'},
                label=''
            ),
            'file': forms.FileField(label=''),
            'body': forms.CharField(widget=CKEditorUploadingWidget(),label=''),
        }
