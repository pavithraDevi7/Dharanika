from django.urls import path
from.views import *


urlpatterns=[
    path('home/',homepage),
    path('students_form/',students_form, name='students_form'),
    path('signup_view/',signup_view, name='signup'),
    path('login_view/',login_view, name='login'),
    path('student_biodata/',student_biodata, name='student_biodata'),
]
