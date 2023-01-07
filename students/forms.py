from django import forms
from .models import Students


class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'age', 'address', 'grade', 'major']

        # labels = {
        #     'student_number': 'Student Number',
        #     'first_name': 'First Name',
        #     'last_name': 'Last Name',
        #     'email': 'Email',
        #     'field_of_study': 'Field of Study'
        # }

        widgets={
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'age': forms.NumberInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'grade': forms.TextInput(attrs={'class':'form-control'}),
            'major': forms.TextInput(attrs={'class':'form-control'}),
        }

