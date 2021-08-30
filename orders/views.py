from django.shortcuts import render

from .models import Data, Order
from .forms import DataModelForm



def upload_file(request):
  form = DataModelForm(request.POST or None, request.FILES or None)
  if form.is_valid():
    form.save()
    # reset it
    form = DataModelForm()
    # fetch unentered data
    unentered = Data.objects.get(entered=False) 

    with open(unentered.file_name.path, 'r', encoding='latin-1') as file:
      
      Order.objects.from_csv(file, dict(invoice_no = 'InvoiceNo', stock_code='StockCode', description='Description', quantity='Quantity', customer_id='CustomerID', unit_price='UnitPrice', country='Country'))
      unentered.entered=True
      unentered.save()
  return render(request, 'orders/upload_file.html', {'form': form})

