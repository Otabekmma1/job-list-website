from .models import Yonalish, Vacancy, Area
from django.shortcuts import render, redirect
from django.contrib import messages

def index(request):
    vacancies = Vacancy.objects.all()
    three_vacan = Vacancy.objects.all()[0:3]
    yonalishlar = Yonalish.objects.all()
    areas = Area.objects.all()

    ctx = {
        'vacancies': vacancies,
        'yonalishlar': yonalishlar,
        'areas': areas,
        'three_vacan': three_vacan
    }
    return render(request, 'blog/index.html', ctx)

def view_all(request):
    vacancies = Vacancy.objects.all()
    three_vacan = Vacancy.objects.all()[0:3]
    yonalishlar = Yonalish.objects.all()
    areas = Area.objects.all()

    ctx = {
        'vacancies': vacancies,
        'yonalishlar': yonalishlar,
        'areas': areas,
        'three_vacan': three_vacan
    }
    return render(request, 'blog/all_vacan_view.html', ctx)


def yunalish(request, yonalish_id):
    vacancies = Vacancy.objects.filter(yonalish_id=yonalish_id)
    yonalishlar = Yonalish.objects.all()
    areas = Area.objects.all()

    ctx = {
        'vacancies': vacancies,
        'yonalishlar': yonalishlar,
        'areas': areas
            }
    return render(request, 'blog/by_category.html', ctx)

def area(request, addres_id):
    vacancies = Vacancy.objects.filter(addres_id=addres_id)
    yonalishlar = Yonalish.objects.all()
    areas = Area.objects.all()

    ctx = {
        'vacancies': vacancies,
        'yonalishlar': yonalishlar,
        'areas': areas,
            }
    return render(request, 'blog/by_area.html', ctx)









def add_vacancy(request):
    vacancies = Vacancy.objects.all()
    yonalishlar = Yonalish.objects.all()
    areas = Area.objects.all()

    if request.method=="POST":
        name = request.POST.get('name')
        yonalish = request.POST.get('yonalish')
        company_name =request.POST.get('company_name')
        required_work_experience = request.POST.get('required_work_experience')
        requirements  = request.POST.get('requirements')
        addres  = request.POST.get('addres')
        salary = request.POST.get('salary')
        category_instance = Yonalish.objects.get(name=yonalish)
        addres_instance = Area.objects.get(name=addres)
        query=Vacancy(name=name,yonalish=category_instance, company_name=company_name, required_work_experience=required_work_experience,
                   requirements=requirements, addres=addres_instance, salary=salary)
        query.save()
        messages.info(request,"E'lon muvaffaqiyatli qo'shildi")
        return redirect("/insert")
    ctx = {
        'vacancies': vacancies,
        'yonalishlar': yonalishlar,
        'areas': areas
    }
    return render(request,"blog/add.html", context=ctx)


def updateVacancy(request,id):
    yonalishlar = Yonalish.objects.all()
    if request.method=="POST":
        name = request.POST.get('name')
        yonalish = request.POST.get('yonalish')
        company_name = request.POST.get('company_name')
        required_work_experience = request.POST.get('required_work_experience')
        requirements = request.POST.get('requirements')
        addres = request.POST.get('addres')
        salary = request.POST.get('salary')
        category_instance = Yonalish.objects.get(name=yonalish)
        addres_instance = Area.objects.get(name=addres)

        edit= Vacancy.objects.get(id=id)
        edit.name=name
        edit.yonalish=category_instance
        edit.company_name=company_name
        edit.required_work_experience = required_work_experience
        edit.requirements = requirements
        edit.addres = addres_instance
        edit.salary = salary
        edit.save()
        messages.warning(request,"E'lon muvaffaqiyatli o'zgartirildi")
        return redirect("/insert")
    vacancy =Vacancy.objects.get(id=id)
    context={
        "vacancy": vacancy,
        'yonalishlar': yonalishlar
    }
    return render(request,"blog/edit.html",context)

def deleteVacancy(request,id):
    vacancy =Vacancy.objects.get(id=id)
    vacancy.delete()
    messages.error(request,"E'lon o'chirildi")
    return redirect("/insert")
