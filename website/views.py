from django.shortcuts import render, HttpResponse
from website.models import Signup,Cart
from django.contrib import messages

# Create your views here.
def home(request):
    context = {
        'websiteName':"Apple Website Clone"
    }
    #context contains variables whom, value can be provided dynamically
    return render(request,'home.html',context)
    # return HttpResponse("This is Home Page!")
    
def pricing(request):
    messages.success(request, 'You are at pricing page')
    return render(request,'pricing.html')
    # return HttpResponse("This is Pricing Page!")

def checkout(request):
    iphone = None
    space = None
    price = None
    total = '$700'
    produts = '2'

    if request.method == 'POST':
        if request.POST.get('base') == "base":
            iphone = "Iphone 14"
            space = "128 GB"
            price = "$1500"
            total = "$2200"
            produts = '3'
        
        if request.POST.get('pro') == "pro":
            iphone = "Iphone 14 Pro"
            space = "256 GB"
            price = "$1700"
            total = "$2400"
            produts = '3'

        if request.POST.get('pro max') == "pro max":
            iphone = "Iphone 14 Pro Max"
            space = "512 GB"
            price = "$2000"
            total = "$2700"
            produts = '3'


    print(space)
    context = {
        'iphone':iphone,
        'space':space,
        'price':price,
        'total':total,
        'produts': produts
    }   
    return render(request,'checkout.html',context)
    # return HttpResponse("This is Checkout Page!")
    # messages.debug(request, "%s SQL statements were executed." % count)
    # messages.info(request, "Three credits remain in your account.")
    # messages.success(request, "Profile details updated.")
    # messages.warning(request, "Your account expires in three days.")
    # messages.error(request, "Document deleted.")

def thanks(request):
    if request.method == "POST":
        FirstName = request.POST.get('firstName')
        LastName = request.POST.get('lastName')
        Email = request.POST.get('email')
        Address = request.POST.get('address')
        PaymentMethod = request.POST.get('paymentMethod')
        #import Model and then make a object of it by passing values recieved earlier
        signup = Signup(FirstName=FirstName, LastName= LastName, Email=Email, Address=Address, PaymentMethod=PaymentMethod)  
        #save the query
        signup.save()
        messages.success(request, 'You have Successfully Signed Up!')

    return render (request,'thanks.html')