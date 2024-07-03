from django.shortcuts import render ,redirect
from .forms import *
from .models import *
from django.contrib import messages
# Create your views here.

def Photo(request):
    images= PhotoUploader.objects.all()
    if request.method =='POST':
            formData=PhotoForm(request.POST ,request.FILES)
            if formData.is_valid():
                  formData.save()
                  messages.add_message(request, messages.SUCCESS, "Product Added Successfully !")
                  return redirect('/image/photo')
            else:
                messages.add_message(request, messages.ERROR, "Failed to add Product ! Please Verify " )
    context={
          'image':images,
          'forms':PhotoForm,
    }
    return render(request,'Images.html',context)
 

# def show_photo(request):
#       images=PhotoUploader.objects.all()

#       context={
            
#       }
#       return(request,'Images.html',context)
      