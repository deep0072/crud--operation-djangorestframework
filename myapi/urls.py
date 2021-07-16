
from django.urls import path, include
from .views import *

urlpatterns = [

    path("", getnotes, name="gets"),

    path("get/<str:pk>/", getnote, name="get"),

    path("create/", create_note, name="create"),

    path("update/<str:pk>/", update_note, name="update"),
    path("delete/<str:pk>/", delete_note, name="delete")

]
