from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html", locals())

def translate(request):
    return render(request, "translate.html", locals())

def contact(request):
    return render(request, "contact.html", locals())
