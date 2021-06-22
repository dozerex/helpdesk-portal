from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Avg

from .models import Complaint
from django.contrib.auth.models import User
from .forms import LoginForm, ComplaintForm


# Create your views here.
@login_required(login_url='login')
def homeView(request):
    complaints = Complaint.objects.filter(is_solved=False)
    return render(request, "complaints/home.html", {
        "complaints": complaints
    })


@login_required(login_url='login')
def createView(request):
    if request.method == "POST":
        form = ComplaintForm(request.POST, request.FILES)
        if form.is_valid():
            Complaint.objects.create(
                title=form.cleaned_data.get("title"),
                urgency=form.cleaned_data.get("urgency"),
                text=form.cleaned_data.get("text"),
                location=form.cleaned_data.get("location"),
                user=User.objects.get(username=request.user.username),
                image=request.FILES["image"]
            )
            return redirect("home")

    else:
        form = ComplaintForm()

    return render(request, "complaints/create.html", {
        "form": form
    })


@login_required(login_url='login')
def detailView(request, id):
    complaint = get_object_or_404(Complaint, id=id)
    return render(request, "complaints/detail.html", {
        "complaint": complaint
    })


def loginView(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("home")

            messages.info(request, "Username or Password is Incorrect")

    else:
        form = LoginForm()

    return render(request, "complaints/login.html", {
        "form": form
    })


@login_required(login_url='login')
def logoutView(request):
    logout(request)
    return redirect("login")


# @login_required(login_url='login')
# def your_complaints(request):
#     user = User.objects.get(username=request.user.username)
#     complaints = Complaint.objects.filter(is_solved=False, user=user)
#     total_complaints = complaints.count()
#     avg_severity = complaints.aggregate(Avg("severity"))
#     return render(request, "complaints/your_complaints.html", {
#         "complaints": complaints,
#         "total": total_complaints,
#         "avg_severity": avg_severity
#     })
