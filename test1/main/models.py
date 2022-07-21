from django.db import models

# Create your models here.
sinf_raqam = (
    ('1', '1-sinf'),
    ('2', '2-sinf'),
    ('3', '3-sinf'),
    ('4', '4-sinf'),
    ('5', '5-sinf'),
    ('6', '6-sinf'),
    ('7', '7-sinf'),
    ('8', '8-sinf'),
    ('9', '9-sinf'),
    ('10', '10-sinf'),
    ('11', '11-sinf'),
)
class Maktab(models.Model):
    name = models.CharField(verbose_name="Maktab raqami", max_length=5)
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}-maktab"

class Talaba(models.Model):
    f_name = models.CharField(max_length=300, verbose_name="F.I.SH")
    maktab = models.ForeignKey(Maktab, on_delete=models.SET_NULL, null=True)
    sinf_raqam = models.CharField(max_length=20, choices=sinf_raqam, default='1-sinf')
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.f_name} {self.maktab}" 

    @property
    def update_sinf_raqam(self):
        pass


    
