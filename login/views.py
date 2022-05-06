from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

teste = messages

from .forms import CreateUserForm

# Creating the comunication with form the user
def registerPage(request):
    if request.user.is_authenticated: # check if the user is logged in
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

        context = {'form': form}
        return render(request,'account/register.html', context)



# function for login

def loginPage(request):
    if request.user.is_authenticated: # check if the user is logged in
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                teste.error(request, "Username OR Password is Incorrect")
    
        context = {}
        return render(request,'account/login.html', context)


#finished the comunication user with system
def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')

#Page Home
def homePage(request):
    context = {}
    return render(request,'account/home.html', context)
