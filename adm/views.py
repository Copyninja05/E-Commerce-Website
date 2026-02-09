from django.shortcuts import render,get_object_or_404,redirect
from .models import product
from django.contrib.auth import authenticate,login,logout
from .models import *


from django.http import HttpResponse
from django.contrib.auth.models import User

def make_admin(request):
    user = User.objects.get(username="admin")  # un username
    user.is_staff = True
    user.is_superuser = True
    user.set_password("admin123")  # fresh password
    user.save()
    return HttpResponse("Admin access granted")




# Create your views here.
def index(request):
    flash_sale=product.objects.filter(sections='flash')
    best_selling=product.objects.filter(sections='best')
    explore=product.objects.filter(sections='explore')

    products=product.objects.all()


   

    return render(request,'index.html',{
        'flash_sale':flash_sale,
        'best_selling':best_selling,
        'explore':explore,
        'products':products
        
    })

def whistledelete(request,id):
    whistle.objects.filter(id=id).delete()
    return redirect('whistle')


def add_to_whistle(request,id):
    #  products = product.objects.get(id=id)

    #  whistle.objects.create(
    #       user=request.user,
    #       products=products
    #  )

    if not request.user.is_authenticated:
         return redirect('login')
    products=product.objects.get(id=id)

    whistle.objects.create(
          user=request.user,
          products=products
     )
    
    return redirect('whistle')

def add_to_carts(request,id):
    products=product.objects.get(id=id)

    cart_items,create=add_to_cart.objects.get_or_create(user=request.user,products=products)

    if not create:
        cart_items.quantity +=1
        cart_items.save()

    return redirect('cart')
    

    

def about(request):
    return render(request,'about.html')
def checkout(request):
     items= add_to_cart.objects.filter(user=request.user)
     if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        street=request.POST.get('street')
        apartment=request.POST.get('apartment')
        city=request.POST.get('city')
        number=request.POST.get('number')
        email=request.POST.get('email')

        if fname=="" or street=="" or apartment=="" or city=="" or number=="" or email=="":
            return render(request,'checkout.html',{'error':'kindly enter all the fields','items':items})
        
        else:
            checkoutdetails.objects.create(
                    fname=fname,
                    lname=lname,
                    street=street,
                    apartment=apartment,
                    city=city,
                    number=number,
                    email=email
            )

            return redirect('success')
            
            
           
            
     return render(request,'checkout.html',{'items':items})
     
            

       

   

    


def cart(request):
     
     items= add_to_cart.objects.filter(user=request.user)
     return render(request,'cart.html',{'items':items})


def whistles(request):
    items= whistle.objects.filter(user=request.user)
    best_selling=product.objects.filter(sections='best')
    return render(request,'whistle.html',{'items':items,'best_selling':best_selling})
   
   
def contacts(request):
    if request.method=='POST':
         print('hello')
         name=request.POST.get('name')
         number=request.POST.get('number')
         email=request.POST.get('email')
         message=request.POST.get('message')

         if name=="" or number=="" or email=="" or message=="":
          print('hello')
          return render(request,'contact.html',{'error':'enter all the field'})
          
    
         if User.objects.filter(username=email).exists():
          contactdetails.objects.create(
            name=name,
            mobilenum=number,
            email=email,
            message=message
          )
          return render(request,'contact.html',{'error':'your message is send'})
         else: 
          return render(request,'contact.html',{'error':'email does not match'})
    
        

    return render(request,'contact.html',{'saved':'your message is send'})


    

    
def signup(request):
    if request.method=='POST':
        
        username = request.POST.get('name') 
        password = request.POST.get('Password')
        Conformpassword = request.POST.get('Conformpassword')
            

        if  username =="" or password=="":
              return render(request,'signup.html',{'error':'kindly enter all fields'})
        
        if password != Conformpassword:
                return render(request,'signup.html',{'error':'password and conformpassword mismatch'})
                
            
        if  User.objects.filter(username=username).exists():
                return render(request,'signup.html',{'error':'username already exists'})
            
        User.objects.create_user(
                username=username,
                password=password
               
            )


        return redirect('/login')
            
         
    
    return render(request, 'signup.html')
  





def login_view(request):
    if request.method=='POST':
         username = request.POST.get('username')
         password = request.POST.get('password')

         user = authenticate(request, username=username, password=password)

         if user is not None:
            login(request,user)
            return redirect('about')
         
         else:
             return render(request, 'login.html',{'error' : 'Invalid credientials'})
    
    return render(request,'login.html')





def products(request,id):
    flash_sale=product.objects.filter(sections='flash')
    best_selling=product.objects.filter(sections='best')
    explore=product.objects.filter(sections='explore')
    single_product = get_object_or_404(product, id=id)

   

    return render(request,'viewproduct.html',{
        'flash_sale':flash_sale,
        'best_selling':best_selling,
        'explore':explore,
        'product':single_product
    })

def success(request):
    return render(request,'success.html')