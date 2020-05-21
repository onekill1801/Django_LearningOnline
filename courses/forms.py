from django import forms

class CreateCourserForm(forms.Form):
    nameCourser = forms.CharField(required=True, max_length=50)
