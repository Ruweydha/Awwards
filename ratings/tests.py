from django.test import TestCase
from .models import Ratings,Profile, Project 
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.user = User(username = 'rue')
        self.user.save()
        self.ruweydha = Profile(user = self.user, id = self.user.profile.id, bio = 'I love coding', profile_pic = 'rue.png', contact = '0767543211')
        
    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()        

    def test_instance(self):
        self.assertTrue(isinstance(self.ruweydha, Profile))

    def test_saveProfile(self):
        self.ruweydha.save_profile()
        profile_saved = Profile.objects.all()
        self.assertTrue(len(profile_saved) > 0)


class ProjectTestClass(TestCase):
    def setUp(self):
        self.user=User(username='aisha')
        self.user.save()
        self.project=Project(image='default.png',title = 'Insta clone',description='A clone of instagram.',profile=self.user.profile, project_url = 'instagram.com')   

    def tearDown(self):
        Project.objects.all().delete()
        Profile.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.project, Project))

    def test_saveProject(self):
        self.project.save_project()
        project_saved = Project.objects.all()
        self.assertTrue(len(project_saved) > 0)