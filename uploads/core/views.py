from django.shortcuts import render
from django.core.files.storage import FileSystemStorage





def home(request):
    print('Home')
    return render(request, 'home.html')


def your_orders(request):
    print('Your Orders')
    return render(request, 'your_orders.html')


def contact(request):
    print('Contact')
    return render(request, 'contact.html')

def test(request):
    print('Test')
    return render(request, 'test.html')

def order_pizza(request):
    print('Order pizza!')
    return render(request, 'order_pizza.html')

