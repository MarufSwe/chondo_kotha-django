from django.contrib import admin

from .models import *


# @admin.site.register(ChondoKotha)
# class ChondoKothaAdmin(admin.ModelAdmin):
#     list_display = ['name']


# admin.site.register(ChondoKotha, ChondoKothaAdmin)
admin.site.register(ChondoKotha)
admin.site.register(Category)
admin.site.register(District)
admin.site.register(Division)
