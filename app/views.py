from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.views import View
from .models import MenuItem


def index(request):
    """View function for home page of site."""
    context = {
    }
    return render(request, 'index.html', context=context)


class DishDetail(View):
    def get(self, request):
        context = {
        }
        return render(request, "dishdetails.html", context)

