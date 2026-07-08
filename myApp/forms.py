from django import forms
from myApp.models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = productModel
        fields = '__all__'

        widgets = {
            'Date': forms.DateInput(attrs = {
                'type':'date',
                'class':'form-control'
            })
        }

        widgets = {
            'Description' : forms.TextInput(attrs = {
            'rows': 3,
            'placeholder': 'Enter product Description'
            })
        }



















        
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     for field in self.fields.values():
    #         field.widget.attrs.update({
    #             'class': 'form-control'
    #         })

    #         self.fields['Description'].widget.attrs.update({
    #             'rows': 3,
    #             'placeholder': 'Enter product Description'
    #         })  