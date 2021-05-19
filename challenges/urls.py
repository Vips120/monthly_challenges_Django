from django.urls import path
from . import views

urlpatterns = [
    # path("january", views.index),
    # path("february", views.feb),
    path("", views.index, name="index"),
    path("<int:month>", views.Monthly_Challenge_By_Number),
    path("<str:month>", views.Monthly_Challenges, name="month-challenge")
]
