from django.urls import path
from . import views

urlpatterns = [
    path('learndj/',views.learn_djanog),
    path('learnpy/',views.learn_python),
]
