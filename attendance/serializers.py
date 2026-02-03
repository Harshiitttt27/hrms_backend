from rest_framework import serializers
from .models import Attendance
from employees.models import Employee

class AttendanceSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format="%Y-%m-%d")
    created_at = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)
    employee_id = serializers.CharField(write_only=True)  # accept employee_id string

    employee = serializers.PrimaryKeyRelatedField(read_only=True)  # keep original FK for output

    class Meta:
        model = Attendance
        fields = ['id', 'employee', 'employee_id', 'date', 'status', 'created_at']

    def validate(self, attrs):
        employee_id = attrs.pop('employee_id')  # remove from attrs and find Employee
        try:
            employee = Employee.objects.get(employee_id=employee_id)
        except Employee.DoesNotExist:
            raise serializers.ValidationError({"employee_id": "Employee with this ID does not exist."})
        
        # check duplicate attendance
        date = attrs.get('date')
        if Attendance.objects.filter(employee=employee, date=date).exists():
            raise serializers.ValidationError("Attendance for this employee on this date already exists.")
        
        attrs['employee'] = employee  # assign actual employee instance
        return attrs
