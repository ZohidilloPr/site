from django.db import models as m

# Create your models here.

length = 250
mM = m.Model
yesNo = (
    ("Bor", "Bor"),
    ("Yoq", "Yoq"), 
)

class DistrictAndCity(mM):
    """ Tuman va Shahar nomlari """
    name = m.CharField(max_length=length, verbose_name="Tuman yoki Shaxar nomi", unique=True)
    add_time = m.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def all_student_in_town(self):
        """ Shaxardagi barcha talabalar """
        all_student = self.students_set.all().count()
        return all_student

class Neighborhood(mM):
    """ Tuman va Shahar dagi barcha mahallalar """
    name = m.CharField(max_length=length, verbose_name="Mahalla nomi")
    districtandcity = m.ForeignKey(DistrictAndCity, on_delete=m.SET_NULL, null=True, verbose_name="Qaysi tuman (shaxar)da joylashgan")
    add_time = m.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def all_student_in_neighborhood(self):
        """ Barcha talabalar """
        all_students = self.students_set.all().count()
        return all_students

class College(mM):
    """ Tuman va Shahardagi barcha kollegelar """
    name = m.CharField(max_length=length, verbose_name="Kollej nomi", unique=True)
    districtandcity = m.ForeignKey(DistrictAndCity, on_delete=m.SET_NULL, null=True)
    add_time = m.DateTimeField(auto_now_add=True)

    def __str__(self):  
        return self.name

class School(mM):
    """ Barcha maktablar """
    number = m.IntegerField(verbose_name="Maktab raqami")
    districtandcity = m.ForeignKey(DistrictAndCity, on_delete=m.SET_NULL, null=True)
    add_time = m.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.number}-umumiy ta'lim maktbi" 

class University(mM):
    """ OTM nomlari """
    name = m.CharField(max_length=length, verbose_name="OTM nomi", unique=True)
    add_time = m.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Interest(mM):
    """ Qiziqishlar """
    name = m.CharField(verbose_name="Qiziqish nomi", max_length=length, unique=True)
    add_time = m.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Opportunity(mM):
    """ Imkonyatlar """
    name = m.CharField(max_length=length, verbose_name="Imkonyatlar nomi", unique=True)
    add_time = m.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Foreign_language(mM):
    """ Chet tilari """
    name = m.CharField(max_length=length, verbose_name="Chet tili nomi", unique=True)
    add_time = m.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Students(mM):
    """ Talabalar """
    f_name = m.CharField(max_length=length, verbose_name="F.I.O")
    student_img = m.ImageField(upload_to='student_images/')
    email = m.EmailField(max_length=length, verbose_name="E-Pochta")
    birth_day = m.DateField(verbose_name="Tug'ulgan sana")
    districtandcity = m.ForeignKey(DistrictAndCity, on_delete=m.SET_NULL, null=True, verbose_name="Yashaydigan tumani")
    neighborhood = m.ForeignKey(Neighborhood, on_delete=m.SET_NULL, null=True, verbose_name="Yashaydigan mahalla")
    driver_l = m.CharField(max_length=length, choices=yesNo, default="Yoq", verbose_name="Haydovchilik guvohnomasi")
    idea = m.CharField(max_length=length, choices=yesNo, default="Bor", verbose_name="Bizsess g'oya")
    interest = m.ManyToManyField(Interest, related_name="interest", verbose_name="Qiziqishlar")
    opportunity = m.ManyToManyField(Opportunity, related_name="opportunity", verbose_name="Imkonyatlari")
    foreign_language = m.ManyToManyField(Foreign_language, related_name="foreign_language", verbose_name="Chet tili")
    add_time = m.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.f_name
