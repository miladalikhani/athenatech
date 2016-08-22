from django.shortcuts import render, redirect
from  django.http import HttpResponse
from forms import SignupForm, LoginForm
from  models import Account


# Create your views here.


def index(request):
    return render(request, 'athenatech/index.html')


def singup(request):
    thisUsername = "not setted"
    thisPassword = "not setted"
    thisEmail = "not setted"
    if request.method == "POST":
        my_signup_form = SignupForm(request.POST)
        if my_signup_form.is_valid():
            thisUsername = my_signup_form.cleaned_data['username']
            thisPassword = my_signup_form.cleaned_data['password']
            password_confrim = my_signup_form.cleaned_data['password_confirm']
            thisEmail = my_signup_form.cleaned_data['email']
            if password_confrim == thisPassword:
                try:
                    account = Account.objects.get(username=thisUsername)
                except:
                    account = Account()
                    account.username = thisUsername
                    account.password = thisPassword
                    account.email = thisEmail
                    account.save()
                    return redirect(index)
            return redirect(index)
    else:
        my_signup_form = SignupForm()
        return redirect(index)


def login(request):
    thisUsername = ""
    thisPassword = ""
    if request.method == "POST":
        my_login_form = LoginForm(request.POST)
        if my_login_form.is_valid():
            thisUsername = my_login_form.cleaned_data['username']
            thisPassword = my_login_form.cleaned_data['password']
            try:
                account = Account.objects.get(username=thisUsername)
                if (account.password == thisPassword):
                    request.session['username'] = thisUsername
                    request.session['password'] = thisPassword
                    return HttpResponse("you are logged in " + thisUsername + " with password " + thisPassword)
                else:
                    return redirect(index)
            except:
                return redirect(index)
    else:
        my_signup_form = SignupForm()
        return redirect(index)

def get_login(request):
    thisUsername = ""
    thisPassword = ""
    if request.method == "GET":
        if ('password' in request.GET) and ('username' in request.GET ):
            print(request.GET)
            thisPassword = request.GET['password']
            thisUsername = request.GET['username']
            try:
                account = Account.objects.get(username=thisUsername)
                if (account.password == thisPassword):
                    return HttpResponse("you are logged in " + thisUsername + " with password " + thisPassword)
                else:
                    return redirect(index)
            except:
                return redirect(index)
    else:
        return HttpResponse("hello")

def test_get(request):
    return render(request, "athenatech/testget.html")


def receive(request):
    if 'milad' in request.GET:
        message = "milad is : " + request.GET['milad']
    else:
        message = "there is no milad in this request"
    return HttpResponse(message)

