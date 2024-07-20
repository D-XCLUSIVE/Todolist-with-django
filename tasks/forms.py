from django import forms

class Addtask(forms.Form):
    title = forms.CharField(max_length=35)
    description = forms.CharField(max_length=350)
    due_date = forms.DateField()
    due_time = forms.TimeField()
    completed = forms.BooleanField()

