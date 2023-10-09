from django import forms
from django.shortcuts import render

from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

class askForInput(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="password")
    

def index(request):
    if "myapp" not in request.session:
        request.session["myapp"] = []
        
        
        
    return render(request,"myapp/index.html",{
        "myapp": request.session["myapp"]
        })
    
    
def add(request):
    
    if request.method == "POST":
        form = askForInput(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            
           
            
            request.session["myapp"] += [username]
            request.session["myapp"] += [password]
            
            return HttpResponseRedirect(reverse("myapp:index"))
        
        else:
            return render(request, "myapp/add.html",{
                "form":form
            })
        
    return render(request,"myapp/add.html",
        {"form": askForInput()
    })