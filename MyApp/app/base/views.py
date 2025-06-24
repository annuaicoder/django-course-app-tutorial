from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from . import models
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    courses = models.Course.objects.all()
    context = {
        "courses": courses,
    }
    return render(request,"base/home.html",context)

def Register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            redirect("login.html")

    else:
        form = UserCreationForm()

    context = {
        "form": form,
        }

    return render(request,"base/register.html",context)

def About(request):
    return render(request,"base/about.html")

def course_detail(request, course_id):
    course = get_object_or_404(models.Course, id=course_id)
    context = {
        "course": course,
    }
    return render(request, "base/course.html", context)