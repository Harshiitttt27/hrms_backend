from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeListCreateView(APIView):

    def get(self, request):
        employees = Employee.objects.all()
        
        if not employees.exists():
            return Response(
                {
                    "message": "No employees found",
                    "count": 0,
                    "data": []
                },
                status=status.HTTP_200_OK
            )

        serializer = EmployeeSerializer(employees, many=True)

        return Response(
            {
                "message": "Employees fetched successfully",
                "count": employees.count(),
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            employee = serializer.save()
            return Response(
                {
                    "message": "Employee created successfully",
                    "data": EmployeeSerializer(employee).data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "message": "Employee creation failed",
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )


class EmployeeDeleteView(APIView):

    def delete(self, request, employee_id):
        try:
            emp = Employee.objects.get(employee_id=employee_id)
            emp_data = EmployeeSerializer(emp).data  
            emp.delete()
            return Response(
                {
                    "message": "Employee deleted successfully",
                    "data": emp_data
                },
                status=status.HTTP_200_OK
            )
        except Employee.DoesNotExist:
            return Response(
                {
                    "message": "Employee not found",
                    "data": {}
                },
                status=status.HTTP_404_NOT_FOUND
            )