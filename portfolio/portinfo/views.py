from django.shortcuts import render
from portinfo.models import Experience

# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    experiences = Experience.objects.all()
    context = {"experiences": experiences}
    return render(request, "about.html", context)

def projects(request):
    return render(request, "projects.html")

def outreach(request):
    return render(request, "outreach.html")

def art(request):
    return render(request, "art.html")