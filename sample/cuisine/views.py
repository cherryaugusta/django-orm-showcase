from django.shortcuts import render
from .models import Cuisine

def cuisine_list(request):
    """Display a list of published cuisine posts."""
    cuisines = Cuisine.published.all()
    return render(request, "cuisine/cuisine_list.html", {"cuisines": cuisines})


def cuisine_detail(request, year, month, day, slug):
    """Display a single cuisine post."""
    from django.shortcuts import get_object_or_404
    cuisine = get_object_or_404(Cuisine, slug=slug, publish__year=year, publish__month=month, publish__day=day)
    return render(request, "cuisine/cuisine_detail.html", {"cuisine": cuisine})
