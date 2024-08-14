from django.conf import settings
from django.shortcuts import redirect, render
from accounts.forms import SignUpForm, LogInForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

User = settings.AUTH_USER_MODEL

def register_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hi {username}, Your account was created successfully!")
            new_user = authenticate(username=form.cleaned_data.get("email"),
                                    password=form.cleaned_data.get("password1")
            )
            login(request, new_user)
            return redirect("app:index")

        print("User registed successfully!")
    else: 
        form = SignUpForm()
        print("User cannot be registered")    
    
    context = {
        "form": form,
    }
    return render(request, "registration/sign-up.html", context)

def login_view(request):
    # if request.user.is_authenticated():
    #     return redirect("app:index")
    
    if request.method == "POST":
        form = LogInForm(request.POST)
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)
        except:
            messages.warning(request, f"User with {email} does not exist")

        user = authenticate(request, email=email, password=password)
        print("email", request.POST.get("email"))
        print(password)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in")
            print("Logged in")
            return redirect("app:index")
        else:
            print("not exist")
            messages.warning(request, "User does not exist.")
    else:
        form = LogInForm()
    context = {
        "form": form
    }

    return render(request, "registration/login.html", context)

def logout_view(request):
    logout(request)
    return redirect("accounts:login")