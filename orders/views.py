from django.shortcuts import render

from .models import Data
from orders.models import Order
from .forms import DataModelForm
import csv

# Create your views here.
def upload_file(request):
  form = DataModelForm(request.POST or None, request.FILES or None)
  if form.is_valid():
    form.save()
    # reset it
    form = DataModelForm()
    # fetch unentered data
    unentered = Data.objects.get(entered=False)

    with open(unentered.file_name.path, 'r') as file:
      reader = csv.reader(file)

      for i, row in enumerate(reader):
        print(row)
        if i == 0:
          pass
        else:
          invoice_no = row[0]
          stock_code = row[1]
          description = row[2]
          quantity = row[3]
          invoice_date = row[4]
          unit_price = row[5]
          customerId = row[6]
          country = row[7]

          Order.objects.create(
                              invoice_no=invoice_no,
                              stock_code=stock_code,
                              description=description,
                              quantity=quantity,
                              invoice_date=invoice_date,
                              unit_price=unit_price,
                              customerID=customerId,
                              country=country
                              )
          unentered.enetered=True
          unentered.save()
  return render(request, 'orders/upload_file.html', {'form': form})

