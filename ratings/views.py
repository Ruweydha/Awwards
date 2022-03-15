from email import message
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ratings.models import Profile, Ratings, Project
from .forms import UpdateProfileForm,ProjectForm, RatingForm
from django.core.exceptions import PermissionDenied


# Create your views here.
@login_required(login_url='/accounts/login/')

def home(request):
   current_user = request.user
   projects = Project.objects.all()
   form = RatingForm()
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

def ratings(request, id):
    current_user = request.user
    project = Project.objects.filter(pk = id).first()
    ratings = Ratings.objects.filter(project = project, user = current_user)
    
    if request.method == 'POST':
        if ratings:
            raise PermissionDenied('You have rated this project.')        
        else:
            form = RatingForm(request.POST, request.FILES)
            if form.is_valid():
                rating = form.save(commit = False)
                design = form.cleaned_data['design']
                usability = form.cleaned_data['usability']
                content = form.cleaned_data['content']
                rating.user = current_user
                rating.project = project
                rating.average = (float(design) + float(usability) + float(content)) /3
                rating.save()

            return redirect("home")   

    else:
        form = RatingForm()  

    return render(request, 'ratings.html', {"current_user":current_user , "form":form, "project":project})    

def search_project (request):
    if 'project' in request.GET and request.GET["project"]:
        search_project = request.GET.get("project")
        searched_projects = Project.search_by_title(search_project)
        message = f'{search_project}'

        return render(request, 'search.html',{"message":message,"results": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})





    


    