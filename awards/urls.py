from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from . import views


urlpatterns=[
    path('',views.home,name='home'),
    path('awwards/project/',views.rate_project,name='rate-project'),
    path('awwards/profile',views.view_profile,name='view-profile'),
    path('search/', views.search_project, name='search_project'),
    path('new/project', views.new_project, name='new_project'),
    path('awwardsapi/api/profile/', views.ProfileList.as_view(),name='api-profile'),
    path('awwardsapi/api/project/', views.ProjectList.as_view(),name='api-project'),
    path('awwardsapi/',views.api_page,name='api-page'),
    path('register/',views.register, name='register'),
    path('user_login/', views.user_login, name='login'),


  
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
  