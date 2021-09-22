from django import forms

from .models import AdviseFree


class AdviseFreeForm(forms.ModelForm):
    class Meta:
        model = AdviseFree
        fields = ('name', 'phone', 'email', 'type_product')
