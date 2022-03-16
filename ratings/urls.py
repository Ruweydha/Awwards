from unicodedata import name
from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

import ratings


urlpatterns=[
    path('', views.home, name = 'home' ),
    path('profile/<int:id>', views.profile, name = 'profile'),
    path('update/profile', views.update_profile, name = 'updateProfile'),
    path('post/project', views.post_project, name = 'postProject'),
    path('rating/<int:id>', views.ratings, name = 'ratings'),
    path('search/', views.search_project, name = 'search_project'),
    path('api/project/', views.ProjectList.as_view()),
    path('api/profile/', views.ProfileList.as_view())

    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)