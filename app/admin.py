from django.contrib import admin
from .models import Yonalish, Vacancy, Area

# class AdminVacancy(admin.ModelAdmin):
#     list_display = ('name', 'company', 'required_work_experience', 'addres', 'salary', 'image')
#     search_fields = ('name', 'company')
#     list_filter = ('yonalish',)
#
# class AdminYonalish(admin.ModelAdmin):
#     list_display = ('name',)

admin.site.register(Yonalish)
admin.site.register(Vacancy)
admin.site.register(Area)
