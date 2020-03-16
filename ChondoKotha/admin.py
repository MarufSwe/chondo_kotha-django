from django.contrib import admin

from .models import *


class ChondoKothaAdmin(admin.ModelAdmin):
    list_display = ['title', 'district_name', 'division_name', 'category_name']


admin.site.register(ChondoKotha, ChondoKothaAdmin)
admin.site.register(Category)
admin.site.register(District)
admin.site.register(Division)
