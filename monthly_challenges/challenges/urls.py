from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path('<int:month>', views.monthly_challenge_in_num),
    path("<str:month>", views.monthly_challenge, name="month-challenge"),
]


 