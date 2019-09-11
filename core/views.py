from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from core.forms import ProfileForm

def HomeView(request):
    count= User.objects.count()
    context={
        'count':count
    }
    return render(request,'core/home.html',context)


class ProfileView(TemplateView):
    template_name='core/profile.html'

    def get(self,request):
        form= ProfileForm()
        context={
            'form': form
        }
        return render(request,self.template_name,context)

    def post(self,request,*args,**kwargs):
        form= ProfileForm(request.POST)
        if form.is_valid():
            user= request.user
            user.first_name= form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()
            return redirect('home')
        form= ProfileForm()
        context={
                'form': form
            }
        return render(request, self.template_name, context)






def Signup(request):
    if request.method=='POST':
        form= UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=UserCreationForm()
    context={
        'form':form
    }
    return render(request,'registration/signup.html',context)
