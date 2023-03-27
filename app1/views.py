from django.shortcuts import render
from .models import Customers


# Create your views here.
def home(request):
    # customer = Customers(FirstName='John', LastName='Doe', Address='123 Main St', PhoneRes='1234567890', EnrollDate='2021-01-01', IsActive='1', CreatedBy='admin', UpdatedBy='admin')
    # customer.save()
    customer = Customers.objects.all()
    return render(request, './home.html', {'customer': customer})

