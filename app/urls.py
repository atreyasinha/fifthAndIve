from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth
from .forms import LoginForm

urlpatterns = [
    path('', views.ProductView.as_view(), name='home'),
    path('filter/<slug:data>', views.ProductFilterView.as_view(), name='filter'),
    path('product/<int:pk>', views.Details.as_view(), name='product'),
    path('register/', views.Registration.as_view(), name='register'),
    path('accounts/login/', auth.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth.LogoutView.as_view(next_page='home'), name='logout'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('address/', views.Addresses.as_view(), name='addresses'),
    path('orders/', views.Orders.as_view(), name='orders'),
    path('cart/', views.Cart.as_view(), name='cart'),
    path('cart-details/', views.Cart_Details.as_view(), name='cart-details'),
    path('removed/<int:pk>', views.Remove_Item.as_view(), name='removed'),
    path('checkout/', views.Checkout.as_view(), name='checkout'),
    path('payment/<int:pk>', views.Payment.as_view(), name='payment'),
    path('placed/<int:pk>', views.Placed.as_view(), name='placed'),
    path('chats/', views.Chats.as_view(), name='chats'),
    path('chats/<str:room_name>/', views.Room.as_view(), name='room'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)