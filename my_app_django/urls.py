from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("<str:name>",views.greet,name="greet"),
    path("omar",views.omar,name="say_hello")
]
