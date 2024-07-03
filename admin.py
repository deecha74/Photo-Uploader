from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(PhotoUploader)

class ImageAdmin(admin.ModelAdmin):
    list_display=['id','PhotoName','photo','date']