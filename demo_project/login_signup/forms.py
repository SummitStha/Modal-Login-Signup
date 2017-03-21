from django import forms

from .models import PostEvent

class PostEventForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = PostEvent
        