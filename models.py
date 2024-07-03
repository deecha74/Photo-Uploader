from django.db import models
import os
import random
# Create your models here.
class PhotoUploader(models.Model):
    Photo_Name=models.CharField(max_length=200 ,default='' , blank=True)
    Photo= models.ImageField(upload_to='static/images')
    CreatedDate= models.DateTimeField(auto_now_add=True)

    def save(self):
        prefox = 'web'
        if not self.Photo_Name:  # Only set Photo_Name if it's not already set
            
            self.Photo_Name = os.path.basename(prefox +self.Photo.name )
             
        super(PhotoUploader, self).save()

    def __str__(self) :
        return self.Photo_Name

     
        
