from django.http import JsonResponse
from django.shortcuts import render
from .models import Division, District, Category


# Create your views here.

def index(request):
    return render(request, "index.html")


# api-1 (data)
def data(request):
    context = {
        'division': list(Division.objects.values()),
        'category': list(Category.objects.values()),
    }
    return JsonResponse(context, safe=False)


# api-2 (district)
# query string with filter
def district(request):
    query = District.objects
    if request.GET.get('division'):
        query = query.filter(division=request.GET.get('division'))

    context = {
        'district': list(query.values()),
    }
    return JsonResponse(context, safe=False)
