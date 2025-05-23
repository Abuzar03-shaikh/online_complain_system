from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Complaint
from django.contrib.messages import get_messages









@login_required(login_url='login')
def home(request):
    return render(request,"index.html")

@login_required(login_url='login')
def about(request):
    return render(request,"about.html")

@login_required(login_url='login')
def contact(request):
    return render(request,"contact.html")

@login_required(login_url='login')
def complain(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        description = request.POST.get('description')

        Complaint.objects.create(
            user=request.user,
            category=category,
            description=description
        )
        messages.success(request, 'Your complaint has been submitted successfully! ✅')  # ✅ show message
        return redirect('complain')  # Or to a success page

    return render(request, "complain.html")

@login_required(login_url='login')
def my_complain(request):
    user_complaints = Complaint.objects.filter(user=request.user).order_by('-id')
    return render(request, "my_complain.html", {"complaints": user_complaints})




def login_view(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
           
            return redirect("home")  # Change to your homepage view
        else:
            messages.error(request, "Invalid credentials")
            return redirect("login")

    return render(request, "login.html")




def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Account created successfully. Please login.")
        return redirect("login")

    return render(request, "register.html")


def logout_view(request):
    logout(request)
     #messages.info(request, "Logged out successfully.")
    return redirect("login")


