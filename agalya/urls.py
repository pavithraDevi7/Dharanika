from django.urls import path
from.views import *


urlpatterns=[
    path('home/',homepage),
    path('student_form/',student_form, name='student_form'),
    path('signup_view/',signup_view, name='signup_view'),
    path('login_view/',login_view, name='login_view'),
]
