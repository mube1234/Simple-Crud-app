from django import forms
from employee_register.models import Employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee  #TABLE name
        fields = "__all__"