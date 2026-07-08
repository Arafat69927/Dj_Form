from django.db import models

# Create your models here.

class forkeymodel(models.Model):
    cateogry_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.cateogry_name}'
    

class productModel(models.Model):
    DEPT_TYPE=[
        ('Electronic','Electronic'),
        ('Cloth','Cloth'),
        ('Food','Food')
    ]
    product_name = models.CharField(max_length=100, null=True)
    product_image = models.ImageField(upload_to='media/product', null=True)
    Department = models.CharField(choices=DEPT_TYPE, max_length=100 ,null=True)
    price = models.PositiveIntegerField(null=True)
    Description = models.TextField(max_length=200, null=True)
    Date = models.DateField(null=True)
    quantity = models.PositiveIntegerField(null=True)
    category = models.ForeignKey(forkeymodel, on_delete=models.CASCADE, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def __str__(self):
        return f'{self.product_name}'