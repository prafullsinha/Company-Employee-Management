from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth.models import User
from core.forms import ProfileForm, RegisterForm, AddProfileForm
from .models import Profile, Company
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.hashers import make_password


@login_required()
def ManagerMemberView(request, email):
    post = Profile.objects.get(company_id=email)
    if request.method == "POST":
        form = ProfileForm(request.POST or None, request.FILES or None, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('home')
    else:
        form = ProfileForm(instance=post)
    template = 'core/member.html'
    context = {
        'form': form,
        'post': post
    }
    return render(request, template, context)


class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get(self, request, *args, **kwargs):
        q = Company.objects.all()
        if request.user.is_authenticated:
            count = 0
            for e in q:
                if request.user.username == e.email:
                    count = 1
            if count == 0:
                return redirect('company')
            else:
                return redirect('profile')
        context = {
            'q': q
        }
        return render(request, self.template_name, context)


@method_decorator(login_required, name='dispatch')
class ManagerView(ListView):
    template_name = 'core/manager.html'

    def get(self, request, *args, **kwargs):
        p = Profile.objects.get(user=request.user)
        queryset = Company.objects.all()
        context = {
            'q': queryset,
            'p': p
        }
        return render(request, self.template_name, context)


@method_decorator(login_required, name='dispatch')
class NormalView(ListView):
    template_name = 'core/normal.html'

    def get(self, request, *args, **kwargs):
        p = Profile.objects.get(user=request.user)
        context = {
            'p': p
        }
        return render(request, self.template_name, context)


@method_decorator(login_required, name='dispatch')
class CompanyView(DetailView):
    template_name = 'core/company.html'

    def get(self, request, *args, **kwargs):
        p = Company.objects.all()
        form = AddProfileForm()
        context = {
            'form': form,
            'p': p
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        hashed_password = make_password("database")
        form = AddProfileForm(request.POST)
        if form.is_valid():
            profile = Profile()
            user = User()
            profile = form.save(commit=False)
            profile.cname = request.user.first_name
            profile.save()
            user = User.objects.create(username=form.cleaned_data['email'], password=hashed_password,
                                       first_name=form.cleaned_data['name'])
            user.save()
            return redirect('company')
        else:
            form = AddProfileForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = 'core/profile.html'

    def get(self, request, *args, **kwargs):
        p = Profile.objects.all()
        q = Company.objects.get(email=request.user.username)
        for e in p:
            if e.user == request.user:
                if e.company.type == 'M':
                    return redirect('manager')
                else:
                    return redirect('normal')
        form = ProfileForm()
        context = {
            'form': form,
            'q': q
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        p = Company.objects.get(email=request.user.username)
        profile = Profile()
        picture = Profile.picture
        form = ProfileForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            profile1 = form.save(commit=False)
            profile1.user = request.user
            profile1.name = request.user.first_name
            profile1.company = p
            profile1.save()
            return redirect('profile')
        else:
            form = ProfileForm()
        context = {
            'picture': picture,
            'form': form,
            'p': p
        }
        return render(request, self.template_name, context)


class Signup2(TemplateView):
    template_name = 'registration/signup2.html'

    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create(username=form.cleaned_data['email'],
                                       password=make_password(form.cleaned_data['password1']),
                                       first_name=form.cleaned_data['first_name'])
            login(request, user)
            return redirect('company')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
