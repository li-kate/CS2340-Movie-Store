from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# UserCreationForm: designed to facilitate the creation of user registration forms, 
# specifically to create new user accounts

def signup(request):
    template_data = {}
    template_data['title'] = 'Sign Up'
    if request.method == 'GET':
        template_data['form'] = UserCreationForm()
        return render(request, 'accounts/signup.html',
            {'template_data': template_data})