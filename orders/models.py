from django.db import models
from postgres_copy import CopyManager

# Create your models here.
class Order(models.Model):
  invoice_no = models.CharField(max_length=15, null=True)
  stock_code = models.CharField(max_length=15, null=True)
  description = models.CharField(max_length=100, null=True)
  quantity = models.IntegerField()
  invoice_date = models.DateTimeField(auto_now_add=True, null=True)
  customer_id = models.IntegerField(blank=True, null=True)
  unit_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
  country = models.CharField(max_length=100, null=True)

  objects = CopyManager()

  def __str__(self):
    return self.description


class Data(models.Model):
  file_name = models.FileField(upload_to='csvs')
  uploaded = models.DateTimeField(auto_now_add=True)
  entered = models.BooleanField(default=False)

  class Meta:
        verbose_name_plural = "Data"

  def __str__(self):
    return f"File: {self.pk}"
