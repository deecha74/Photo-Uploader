from django.forms import ModelForm
from .models import PhotoUploader


class PhotoForm(ModelForm):
    class Meta:
        model= PhotoUploader
        fields = ['Photo' , ]
        labels= {'Photo':''}