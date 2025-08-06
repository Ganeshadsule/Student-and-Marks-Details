from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('view_students', views.view_students, name='view_students'),
    path('add_student', views.add_student, name='add_student'),
    path('add_successfully', views.success, name='success'),
 ]