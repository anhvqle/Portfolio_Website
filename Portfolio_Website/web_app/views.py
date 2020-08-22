from django.shortcuts import render
from django.http import HttpResponse, FileResponse, Http404
from web_app.models import Employer
from web_app.forms import NewUserForm

def thankyou(request):
    return render(request, 'thankyou.html')

def resume(request):
    try:
        return FileResponse(open('static/AnhLe_Resume.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

def unity(request):
    try:
        return FileResponse(open('static/Unity.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

def index(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return thankyou(request)
        else:
            print("ERROR FORM INVALID")
    return render(request, 'home.html', {'form' : form})
