from django.db import models as m

# Create your models here.
length = 250
mM = m.Model

class DistrictAndCity(mM):
    name = m.CharField(max_length=length, verbose_name="Tuman yoki Shaxar nomi", unique=True)
    add_time = m.DateTimeField(auto_now_add=True)

class Neighborhood(mM):
    name = m.CharField(max_length=length, verbose_name="Mahalla nomi")
    districtandcity = m.ForeignKey(DistrictAndCity, on_delete=m.SET_NULL, null=True, verbose_name="Qaysi tuman (shaxar)da joylashgan")
    add_time = m.DateTimeField(auto_now_add=True)

class College(mM):
    name = m.CharField(max_length=length, verbose_name="Kollej nomi", unique=True)
    districtandcity = m.ForeignKey(DistrictAndCity, on_delete=m.SET_NULL, null=True)
    add_time = m.DateTimeField(auto_now_add=True)

class School(mM):
    number = m.IntegerField(verbose_name="Maktab raqami")
    districtandcity = m.ForeignKey(DistrictAndCity, on_delete=m.SET_NULL, null=True)
    add_time = m.DateTimeField(auto_now_add=True)

class University(mM):
    name = m.CharField(max_length=length, verbose_name="OTM nomi", unique=True)
    add_time = m.DateTimeField(auto_now_add=True)

class Students(mM):
    f_name = m.CharField(max_length=length, verbose_name="F.I.O")
    student_img = m.ImageField(upload_to='student_images/')
