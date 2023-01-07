from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>', views.view_student, name='view_student'),
    path('add_student/',views.add_student, name='add_student'),
    path('edit_student/<str:id>',views.edit_student, name='edit_student'),
    path('delete_student/<str:id>',views.delete_student, name='delete_student'),
]
