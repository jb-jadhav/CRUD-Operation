from django import forms
from .models import Employee
from django.forms import ModelForm


class EmployeeForm(forms.ModelForm):
    
    class Meta:

        model = Employee
        fields = "__all__"

    def __init__(self,*args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['Position'].empty_lable = "Select" 
        #self.fields['emp_code'].required = False  # not required fields 