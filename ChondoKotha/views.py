from django.http import JsonResponse
from django.shortcuts import render
from .models import Division, District, Category, ChondoKotha


# Create your views here.

def index(request):
    return render(request, "index.html")


# api-1 (data) // Division
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


# api-3
def chondoKotha(request):
    query = ChondoKotha.objects

    if request.GET.get('division'):
        query = query.filter(district__division=request.GET.get('division'))

    if request.GET.get('category'):
        query = query.filter(category=request.GET.get('category'))

    if request.GET.get('district'):
        query = query.filter(district=request.GET.get('district'))

    context = dict(kotha=list(query.values('title', 'category_id', 'district_id', 'category__name', 'district__name',
                                           'district__division__name')))

    return JsonResponse(context, safe=False)
