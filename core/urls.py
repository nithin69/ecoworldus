from django.urls import path
from .views import (
    ItemDetailView,
    CheckoutView,
    HomeView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView,
)
from django.views.decorators.csrf import csrf_exempt
from . import views

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('signup/', views.signup, name='signup'),
    path('categories/', views.categoriesLst, name='categoriesLst'),
    path('detail-product/<slug>/', views.detailCategory, name='detailCategory'),
    path('featured-products/', views.featuredProducts, name='featuredProducts'),
    path('contact/', csrf_exempt(views.contact), name='contact'),
    path('subscribe/', csrf_exempt(views.subscribe), name='subscribe'),
    path('profile/', views.profile, name='profile'),

    # path('accounts/signup/', views.signup, name='signup'),categoriesLst

]
