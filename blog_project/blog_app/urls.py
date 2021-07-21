from django.urls import path,include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('create_post/',views.create_post,name='create_post'),
    path('view_post/',views.view_post,name='view_post'),
    path('accounts/', include('allauth.urls')),
    path('logout/', LogoutView.as_view()),

]