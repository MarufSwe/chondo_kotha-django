from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index),
    path('lazy-eager',views.lazy_loading),
    path('data/',views.data),
    path('district/',views.district),
    path('kotha/',views.chondoKotha),
]
