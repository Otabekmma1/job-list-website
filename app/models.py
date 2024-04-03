from django.db import models

class Yonalish(models.Model):
    name = models.CharField(max_length=100, verbose_name="Yo'nalish")
    image = models.ImageField(upload_to='img/', verbose_name="rasm")

    def __str__(self):
        return self.name


class Area(models.Model):
    name = models.CharField(max_length=100, verbose_name='Shahar')

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    name = models.CharField(max_length=100, verbose_name="Vakansiya")
    yonalish = models.ForeignKey(Yonalish, on_delete=models.CASCADE, verbose_name="Yo'nalish")
    company_name = models.CharField(max_length=100, verbose_name="Kompaniya nomi")
    required_work_experience = models.CharField(max_length=100, verbose_name="Ish tajriba")
    requirements = models.TextField(verbose_name="Talablar")
    addres = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name="Manzil")
    salary = models.IntegerField(verbose_name="Maosh")
    image = models.ImageField(upload_to='img/', verbose_name="Rasm")

    def __str__(self):
        return self.name