from django import forms

from postsApp.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'
