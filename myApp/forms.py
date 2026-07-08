from django import forms
from myApp.models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = productModel
        fields =['product_name','product_image',
                 'Department','price',
                 'Description','Date',
                 'quantity','category']

        widgets = {
            'Date': forms.DateInput(attrs = {
                'type':'date',
                'class':'form-control'
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