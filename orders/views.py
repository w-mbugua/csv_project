from django.shortcuts import render

from .models import Data, Order
from .forms import DataModelForm
import pandas as pd
import time

# Create your views here.
def upload_file(request):
  form = DataModelForm(request.POST or None, request.FILES or None)
  if form.is_valid():
    form.save()
    # reset it
    form = DataModelForm()
    # fetch unentered data
    unentered = Data.objects.get(entered=False) 
    start = time.time()
    with open(unentered.file_name.path, 'r', encoding='latin-1') as file:
      # df = pd.read_csv(file, sep=',')
      # row_iterator = df.iterrows()
      
      Order.objects.from_csv(file, dict(invoice_no = 'InvoiceNo', stock_code='StockCode', description='Description', quantity='Quantity', customer_id='CustomerID', unit_price='UnitPrice', country='Country'))
      unentered.entered=True
      unentered.save()
      end = time.time() - start
      print("That took",end)
  return render(request, 'orders/upload_file.html', {'form': form})

# objs = [

#       Order(
#           stock_code = row['StockCode'],
#           description  = row['Description'],
#           quantity  = row['Quantity'],
#           unit_price  = row['UnitPrice'],
#           country = row['Country']
#       )
#       for index, row in row_iterator
#       ]