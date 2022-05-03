from django.shortcuts import render
from django.views.generic.base import View


class CatalogView(View):
    """Главная страница"""
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, "catalog/catalog.html")
        else:
            return render(request, "registration/login.html")

