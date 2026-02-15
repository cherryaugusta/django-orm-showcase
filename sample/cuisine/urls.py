from django.urls import path
from . import views

app_name = "cuisine"

urlpatterns = [
    path("", views.cuisine_list, name="cuisine_list"),
    path("<int:year>/<int:month>/<int:day>/<slug:slug>/", 
         views.cuisine_detail, name="cuisine_detail"),
]
