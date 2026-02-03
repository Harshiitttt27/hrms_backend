from django.urls import path
from .views import MarkAttendanceView, EmployeeAttendanceView

urlpatterns = [
    path("attendance/", MarkAttendanceView.as_view()),
    path("attendance/<str:employee_id>/", EmployeeAttendanceView.as_view()),
]
