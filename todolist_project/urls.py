from django.urls import path
from todolist_project.views import index


app_name = "todo"

urlpatterns = [
    path("", index, name="index")
]
