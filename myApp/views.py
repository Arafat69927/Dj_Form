from django.shortcuts import render,redirect
from myApp.models import *
from myApp.forms import * 
# Create your views here.
def product_view(req):

    return render(req,'product.html')

def product_list(req):
    product_data = productModel.objects.all()
    context={
        'product_dic':product_data
    }
    return render(req,'product_list.html',context)
 
def add_product(req):
    if req.method == 'POST':
        forms_data = ProductForm(req.POST, req.FILES)
        if forms_data.is_valid():
            product = forms_data.save(commit=False)
            product.total = product.price * product.quantity
            product.save()
        return redirect('product_list')
    else:
       forms_data = ProductForm()

    context={
       'forms_dic':forms_data
    }

    return render(req,'add_product.html',context)

def edit_product(req,myid):
    edit_data = productModel.objects.get(id=myid)
    if req.method == 'POST':
        forms_data = ProductForm(req.POST, req.FILES, instance=edit_data)
        if forms_data.is_valid():
            product = forms_data.save(commit=False)
            product.total = product.price * product.quantity
            product.save()
        return redirect('product_list')
    else:
       forms_data = ProductForm(instance=edit_data)

    context={
       'forms_dic':forms_data
    }

    return render(req,'edit_product.html',context)

def delete_product(req,myid):
    delete_data = productModel.objects.get(id=myid)
    delete_data.delete()
    return redirect('product_list')