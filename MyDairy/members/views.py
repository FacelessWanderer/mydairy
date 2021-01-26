from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.contrib import messages
from .forms import CreateUserForm, EditProfileForm, ProfilePageForm
from django.contrib.auth.views import PasswordChangeView
from main.models import Profile
from  django.views.generic import DetailView, CreateView
# Create your views here.


class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = "registration/initial_profile.html"
        #fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ShowProfilePage(DetailView):
    model = Profile
    template_name = 'registration/myprofile.html'

    def get_context_data(self, *args, **kwargs):
        #users = Profile.objects.all()
        context = super(ShowProfilePage, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context


class EditProfilePageView(generic.UpdateView):
    model = Profile
    #form_class = ProfilePageForm
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'profile_pic']
    success_url = reverse_lazy('home')


class UserRegisterView(generic.CreateView):
    form_class = CreateUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit-profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, 'registration/password_success.html', {})


