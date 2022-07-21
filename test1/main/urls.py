from django.urls import path
from .views import Talaba_function

urlpatterns = [
    path("", Talaba_function, name="HOME")
]