from django.urls import path
from todolist_project.views import index


app_name = "todolist_project"

urlpatterns = [
    path("", index, name="index")
]
