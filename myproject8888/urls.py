from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', views.students, name='students'),
    path('courses/', views.courses, name='courses'),
    path('details/<int:student_id>/', views.details, name='details'),
]
