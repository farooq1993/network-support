from django.urls import path
from .views import submit_student_form,wireless, Login, home, Logout,fungenerate

urlpatterns = [
    path('', Login, name='login'),

    path('register/', submit_student_form, name='submit_student_form'),

    path('wireless/', wireless, name='wireless'),

    path('function_generatore/', fungenerate, name="function_generatore"),
    
    path('home/', home, name='home'),

    path('logout/', Logout, name='logout'),
]
