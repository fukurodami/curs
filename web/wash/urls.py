from unicodedata import name
from django.urls import path, include
from wash import views

urlpatterns = [
    path("", views.CatalogView.as_view()),
]