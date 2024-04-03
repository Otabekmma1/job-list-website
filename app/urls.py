from django.urls import path
from .views import (index, add_vacancy, updateVacancy, deleteVacancy,
                    yunalish, area, view_all)

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:yonalish_id>/', yunalish, name='categories'),
    path('addres/<int:addres_id>/', area, name='areas'),
    path('vacancies/', view_all, name='all_vacan'),
    #crud
    path('insert/', add_vacancy, name="create"),
    path('update/<id>/', updateVacancy, name="updateVacancy"),
    path('delete/<id>/', deleteVacancy, name="deleteVacancy"),
]