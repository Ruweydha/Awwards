from unicodedata import name
from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns=[
    path('', views.home, name = 'home' ),
    path('profile/<int:id>', views.profile, name = 'profile'),
    path('update/profile', views.update_profile, name = 'updateProfile'),
    path('post/project', views.post_project, name = 'postProject')
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)