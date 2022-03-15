from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ratings.models import Profile, Project
from .forms import UpdateProfileForm,ProjectForm

# Create your views here.
@login_required(login_url='/accounts/login/')

def home(request):
   current_user = request.user
   projects = Project.objects.all()
   form = UpdateProfileForm()
   return render(request,'home.html', {"current_user": current_user, "form": form, "projects":projects})

def update_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.save()

        return redirect("profile", id = current_user.id )   

    else:
        form = UpdateProfileForm()  

    return render(request, 'update_profile.html', {"current_user":current_user , "form":form})

def profile(request, id):
    current_user = request.user
    profile = Profile.objects.filter(user = current_user.pk).first()
    projects = Project.objects.filter(profile = profile).all()

    return render (request, 'profile.html', {"profile":profile, "projects":projects})
      
def post_project(request):
    current_user = request.user  
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit = False)
            project.profile = current_user.profile
            project.save()

        return redirect("home")   

    else:
        form = ProjectForm()  

    return render(request, 'post_project.html', {"current_user":current_user , "form":form})    

