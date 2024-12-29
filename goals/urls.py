from django.urls import path
from goals import views

app_name = 'goals'
urlpatterns = [
    path('', views.ChoiceChooser, name='choices'),
    path('submit/', views.ChoiceSubmission, name="submission"),
]