from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,login as auth_login, logout as auth_logout
from django.views.generic import TemplateView

from django.core.urlresolvers import reverse

from django.http import JsonResponse
from django.template.loader import render_to_string
# Create your views here.



class LoginSignup(TemplateView):
    template_name = 'base.html'
    def get_context_data(self, **kwargs):
        context = super(LoginSignup, self).get_context_data(**kwargs)
        context['signup_form'] = UserCreationForm()
        context['login_form'] = AuthenticationForm()
        return context


def user_signup(request):
    template_name = 'signup/user_signup.html'
    data = dict()
    if request.method=="POST":
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            data['form_is_valid'] = True
            username = signup_form.cleaned_data.get('username')
            password = signup_form.cleaned_data.get('password1')
            user =  authenticate(username=username, password=password)
            auth_login(request, user)
            template_name = 'includes/logedin_user.html'
            data['html_user'] = render_to_string(template_name, {'user': user})
        else:
            data['form_is_valid']=False
    else:
        signup_form = UserCreationForm()
    data['html_form'] = render_to_string(template_name, {'signup_form': signup_form}, request=request)
    return JsonResponse(data)
    


def login(request):
    template_name = 'signup/user_login.html'
    data = dict()
    if request.method=="POST":
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            # form.save()
            data['form_is_valid'] = True
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user =  authenticate(username=username, password=password)
            auth_login(request, user)
            template_name = 'includes/logedin_user.html'
            data['html_user'] = render_to_string(template_name, {'user': user})
            return JsonResponse(data)
        else:
            data['form_is_valid']=False
    else:
        login_form = AuthenticationForm()
        
    data['html_form'] = render_to_string(template_name, {'login_form': login_form}, request=request)
    return JsonResponse(data)


def user_login(request):
    template_name='forms/user_login_form.html'
    if request.method=="POST":
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            auth_login(request, user)
    else:
        login_form=AuthenticationForm()

    context = {'form': login_form}

    return render(request, template_name, context)




def user_logout(request):
    template_name = 'signup/user_logout.html'
    data = dict()
    if request.method=='POST':
        
        data['form_is_valid'] = True
        auth_logout(request)
        template_name = 'includes/logedout_user.html'
        # template_name = 'includes/header.html'
        data['html_user'] = render_to_string(template_name, {})
        # return JsonResponse(data)

    else:
        data['html_form'] = render_to_string(template_name, request=request)

    return JsonResponse(data)
