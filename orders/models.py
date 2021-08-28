from django.db import models

# Create your models here.
class Order(models.Model):
  invoice_no = models.CharField(max_length=6, blank=True, null=True)
  stock_code = models.CharField(max_length=6, blank=True, null=True)
  description = models.CharField(max_length=100)
  quantity = models.PositiveIntegerField()
  invoice_date = models.DateTimeField(auto_now_add=True)
  unit_price = models.DecimalField(max_digits=6, decimal_places=2)
  customerID = models.PositiveIntegerField(blank=True, null=True)
  country = models.TextField(blank=True, null=True)

  def __str__(self):
    return f"{self.invoice_no} - {self.description}"


class Data(models.Model):
  file_name = models.FileField(upload_to='csvs')
  uploaded = models.DateTimeField(auto_now_add=True)
  entered = models.BooleanField(default=False)

  def __str__(self):
    return f"File: {self.pk}"
