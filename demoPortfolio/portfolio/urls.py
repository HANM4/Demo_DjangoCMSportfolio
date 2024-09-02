from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', ProjectsListView.as_view(), name='projects'),
    path('<slug:slug>/', ProjectDetailView.as_view(), name='project_page'),
    path('tags/<slug:slug>/', TagProjectsListView.as_view(), name='tag'),
]