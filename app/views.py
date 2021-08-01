from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from .models import Product, Customer, CART, OrderPlaced, ChatLinks
from .forms import RegistrationForm, ProfileForm
from django.contrib.auth.decorators import login_required

class ProductView(View):
    def get(self, request):
        products = list(Product.objects.all())
        chatsLinks = ChatLinks.objects.all()
        return render(request, 'index.html', {'products': products, 'chatsLinks': chatsLinks})

class ProductFilterView(View):
    def get(self, request, data=None):

        if data == 'CS':
            products = Product.objects.filter(category='CS')
        elif data == 'JA':
            products = Product.objects.filter(category='JA')
        elif data == 'HG':
            products = Product.objects.filter(category='HG')
        elif data == 'E':
            products = Product.objects.filter(category='E')
        elif data == 'TECH':
            products = Product.objects.filter(category='TECH')
        else:
            products = Product.objects.filter(category='TO')

        return render(request, 'index.html', {'products': products})

class Details(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'product.html', {'product': product})

class Registration(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'register.html', {'form': form})

@method_decorator(login_required, name="dispatch")
class Profile(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, 'profile.html', {'form': form, 'home_active': 'active'})

    def post(self, request):
        form = ProfileForm(request.POST)
        if form.is_valid():
            customer = request.user
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            street_address = form.cleaned_data['street_address']
            apt_house = form.cleaned_data['apt_house']
            city = form.cleaned_data['city']
            zipcode = form.cleaned_data['zipcode']
            state = form.cleaned_data['state']
            phone_number = form.cleaned_data['phone_number']
            data = Customer(customer=customer, first_name=first_name, last_name=last_name, street_address=street_address, apt_house=apt_house, city=city, zipcode=zipcode, state=state, phone_number=phone_number)
            data.save()

        return render(request, 'profile.html', {
            'form': form, 'home_active': 'active'
        })

@method_decorator(login_required, name="dispatch")
class Addresses(View):
    def get(self, request):
        user_addresses = Customer.objects.filter(customer=request.user)

        return render(request, 'addresses.html', {
            'address_active': 'active', 'user_addresses': user_addresses
        })

@method_decorator(login_required, name="dispatch")
class Orders(View):
    def get(self, request):
        orders = OrderPlaced.objects.filter(user=request.user)

        context = {
            'order_active': 'active',
            'orders': orders
        }
        return render(request, 'orders.html', context)

@method_decorator(login_required, name="dispatch")
class Chats(View):
    def get(self, request):
        return render(request, 'chat.html', {'chat_active': 'active'})

@method_decorator(login_required, name="dispatch")
class Room(View):
    def get(self, request, room_name):
        current_url = request.path_info
        ChatLinks(link=current_url, room=room_name, user=request.user).save()
        ChatLinks.objects.filter(user='admin').delete()

        return render(request, 'room.html', {
            'room_name': room_name,
            'chat_active': 'active'
        })

@method_decorator(login_required, name="dispatch")
class Cart(View):
    def get(self, request):
        customer = request.user
        product_id = request.GET.get("product_id")
        product_instance = Product.objects.get(id=product_id)
        CART(customer=customer, product=product_instance).save()

        return redirect('/cart-details')

@method_decorator(login_required, name="dispatch")
class Remove_Item(View):
    def get(self, request, pk):
        cart = CART.objects.get(pk=pk)
        cart.delete()

        return redirect('/cart-details')

@method_decorator(login_required, name="dispatch")
class Cart_Details(View):
    def get(self, request):
        total_price = 0

        if request.user.is_authenticated:
            cart = CART.objects.filter(customer=request.user)
            total_count = CART.objects.filter(customer=request.user).count()

            for c in cart:
                total_price += c.product.price

            shipping_cost = 0

            if total_price < 75 and total_price > 0:
                total_price += 15
                shipping_cost = 15

            page = 'cart.html'
            context = {
                'cart': cart,
                'total_count': total_count,
                'total_price': total_price,
                'shipping_cost': shipping_cost
            }
            return render(request, page, context)

@method_decorator(login_required, name="dispatch")
class Checkout(View):
    def get(self, request):
        total_price = 0

        if request.user.is_authenticated:
            cart = CART.objects.filter(customer=request.user)
            total_count = CART.objects.filter(customer=request.user).count()
            user_addresses = Customer.objects.filter(customer=request.user)

            for c in cart:
                total_price = total_price + c.product.price

            shipping_cost = 0

            if total_price < 75 and total_price > 0:
                total_price += 15
                shipping_cost = 15

            page = 'checkout.html'
            context = {
                'cart': cart,
                'total_count': total_count,
                'total_price': total_price,
                'user_addresses': user_addresses,
                'shipping_cost': shipping_cost
            }

            return render(request, page, context)

@method_decorator(login_required, name="dispatch")
class Payment(View):
    def get(self, request, pk):
        total_price = 0
        if request.user.is_authenticated:
            cart = CART.objects.filter(customer=request.user)
            total_count = CART.objects.filter(customer=request.user).count()
            address = Customer.objects.get(pk=pk)

            for c in cart:

                total_price = total_price + c.product.price

            shipping_cost = 0

            if total_price < 75 and total_price > 0:
                total_price += 15
                shipping_cost = 15

            context = {
                'cart': cart,
                'total_count': total_count,
                'total_price': total_price,
                'address': address,
                'shipping_cost': shipping_cost
            }

            page = 'payment.html'

            return render(request, page, context)

@method_decorator(login_required, name="dispatch")
class Placed(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            cart = CART.objects.filter(customer=request.user)
            for c in cart:
                OrderPlaced(user=request.user, customer=Customer.objects.get(id=pk), product=c.product, quantity=c.quantity).save()
                c.delete()

            return redirect('/orders')




