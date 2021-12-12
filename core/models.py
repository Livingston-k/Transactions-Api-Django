from django.db import models

# Create your models here.
class Currency(models.Model):
    code = models.CharField(max_length=6,unique=True)
    name = models.CharField(max_length=13,null=True,blank = True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255,blank=True, null=True)
    def __str__(self):
        return self.name

class Transaction(models.Model):
    amount = models.DecimalField(max_digits=15,decimal_places=2)
    currency = models.name = models.ForeignKey('Currency', related_name='transactions', on_delete=models.PROTECT)
    date = models.DateTimeField()
    description = models.TextField(null=True,blank=True)
    category = models.ForeignKey('Category',related_name='transactions',on_delete=models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return f"{self.amount} {self.currency.code} {self.date}"
