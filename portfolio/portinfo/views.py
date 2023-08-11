from django.shortcuts import render
from portinfo.models import *
from django.db.models.functions import Coalesce
from django.db.models import F, Value, Case, When, DateField

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {"articles": articles}
    return render(request, "index.html", context)

def about(request):
    experiences = Experience.objects.annotate(
        ordered_end_date=Coalesce('end_date', Value('9999-12-31', output_field=DateField()))
    ).order_by('-ordered_end_date')

    context = {"experiences": experiences}
    return render(request, "about.html", context)

def projects(request):
    return render(request, "projects.html")

def outreach(request):
    return render(request, "outreach.html")

def art(request):
    return render(request, "art.html")