from django import forms
from .models import Earning

class EarningForm(forms.ModelForm):
    class Meta:
        model = Earning
        fields = ['job_name', 'invoice_number', 'description', 'amount', 'image1', 'image2', 'date']
