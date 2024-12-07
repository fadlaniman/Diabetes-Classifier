from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from .models import Diabetes
from .classification import model
import pandas as pd
 
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/polls/home/')
            else:
                return HttpResponse('Invalid login')
    else:
        form = AuthenticationForm()

    return render(request, 'polls/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/polls/home')

def index(request):
    return render(request, "polls/index.html") 

@login_required
def predict(request):
    context = {'data' : None}
    if request.method == 'POST':
        data = {key: value for key, value in request.POST.items() if key != 'csrfmiddlewaretoken'}
        X_test = pd.DataFrame([data])
        y_pred = model.predict(X_test.values)
        if y_pred == [0] :
            description = 'Negative'
        else:
            description = 'Positif'
        context = {'data' : description}
    return render(request, "polls/predict.html", context) 