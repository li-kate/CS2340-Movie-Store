from django.shortcuts import render
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from .forms import CustomUserCreationForm, CustomErrorList
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import CustomUser 
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import PermissionDenied

@login_required
def logout(request):
    auth_logout(request)
    return redirect('home.index')

def login(request):
    template_data = {}
    template_data['title'] = 'Login'
    
    if request.method == 'GET':
        return render(request, 'accounts/login.html', {'template_data': template_data})
    
    elif request.method == 'POST':
        try:
            user = authenticate(
                request,
                username=request.POST['username'],
                password=request.POST['password']
            )
            if user is None:
                template_data['error'] = 'The username or password is incorrect.'
                return render(request, 'accounts/login.html', {'template_data': template_data})
            else:
                auth_login(request, user)
                return redirect('home.index')
        
        except PermissionDenied:
            # Handle CSRF verification failed error
            template_data['error'] = 'You logged in too quickly. Please go back and log in again.'
            return render(request, 'accounts/login.html', {'template_data': template_data})

def signup(request):
    template_data = {}
    template_data['title'] = 'Sign Up'
    if request.method == 'GET':
        template_data['form'] = CustomUserCreationForm()
        return render(request, 'accounts/signup.html', {'template_data': template_data})
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST, error_class=CustomErrorList)
        if form.is_valid():
            user = form.save()  # Save the user and get the user object
            auth_login(request, user)  # Log the user in after registration
            return redirect('home.index')  # Redirect to the home page or another page
        else:
            template_data['form'] = form
            return render(request, 'accounts/signup.html', {'template_data': template_data})
        
@login_required
def orders(request):
    template_data = {}
    template_data['title'] = 'Orders'
    template_data['orders'] = request.user.order_set.all()
    return render(request, 'accounts/orders.html',
        {'template_data': template_data})