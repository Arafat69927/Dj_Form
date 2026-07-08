from django.db import models

# Create your models here.
class productModel(models.Model):
    DEPT_TYPE=[
        ('Electronic','Electronic'),
        ('Cloth','Cloth'),
        ('Food','Food')
    ]
    product_name = models.CharField(max_length=100, null=True)
    product_image = models.ImageField(upload_to='media/product', null=True)
    Department = models.CharField(choices=DEPT_TYPE, null=True)
    price = models.PositiveIntegerField(null=True)
    Description = models.TextField(max_length=200, null=True)
    def __str__(self):
        return f'{self.product_name}'