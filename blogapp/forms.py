
from django import forms
from blogapp.models import Posts

class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = "__all__"


class UpdateBlogForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = "__all__"