from django.urls import path
from .views import EmployeeListCreateView, EmployeeDeleteView

urlpatterns = [
    path("employees/", EmployeeListCreateView.as_view()),
    path("employees/<str:employee_id>/", EmployeeDeleteView.as_view()),
]
