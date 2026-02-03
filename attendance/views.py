from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Attendance
from .serializers import AttendanceSerializer
from employees.models import Employee

class MarkAttendanceView(APIView):

    def post(self, request):
        serializer = AttendanceSerializer(data=request.data)
        if serializer.is_valid():
            attendance = serializer.save()
            return Response(
                {
                    "message": "Attendance marked successfully",
                    "data": AttendanceSerializer(attendance).data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "message": "Attendance marking failed",
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )

class EmployeeAttendanceView(APIView):

    def get(self, request, employee_id):
        try:
            employee = Employee.objects.get(employee_id=employee_id)
            attendance_records = Attendance.objects.filter(employee=employee)
            
            if not attendance_records.exists():
                return Response(
                    {
                        "message": "No attendance records found for this employee",
                        "count": 0,
                        "data": []
                    },
                    status=status.HTTP_200_OK
                )

            serializer = AttendanceSerializer(attendance_records, many=True)
            return Response(
                {
                    "message": "Attendance records fetched successfully",
                    "count": attendance_records.count(),
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )

        except Employee.DoesNotExist:
            return Response(
                {
                    "message": "Employee not found",
                    "data": []
                },
                status=status.HTTP_404_NOT_FOUND
            )
