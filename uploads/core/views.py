from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


array = []

def home(request):
    print('Home')
    return render(request, 'home.html')


def your_orders(request):
    print('Your Orders')
    return render(request, 'your_orders.html')


def contact(request):
    print('Contact')
    return render(request, 'contact.html')



def order_pizza(request):
    array = []
    for i in range(18):
        i =str(i)
        temp =str('item'+i)
        array.append(str(request.POST.get(temp)))


    print('Order pizza!')
    print(array[0])
    print(array[1])
    print(array[15])
    print(array[16])
    print(array[17])
    
    order = "You ordered pizza with: "
    for i in range(16):
        if array[i]!= 'None':
            order+=(array[i]+", ")
    if order == "You ordered pizza with: ":
        order +="NOTHING  "
    if array[16]!='None' and array[17]!='None':
        order+=(" that is both gluten and lactose free!")
    elif array[16]!='None':
        order+=(" that is gluten free!")
    elif array[17]!='None':
        order+=(" that is lactose free!")
    else:
        order = order[:-2]
        order +="."

    return render(request, 'order_pizza.html', {'test':order})

