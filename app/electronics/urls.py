from django.urls import path
from electronics.views import SupplierCreateAPIView, SupplierRetrieveAPIView, SupplierListAPIView, SupplierUpdateAPIView, SupplierDestroyAPIView, ContactUpdateAPIView, ProductUpdateAPIView

urlpatterns = [
    path('create_suppliers/', SupplierCreateAPIView.as_view(), name='create_suppliers'),
    path('retrive_suppliers/<int:pk>/', SupplierRetrieveAPIView.as_view(), name='retrive_suppliers'),
    path('update_suppliers/<int:pk>/', SupplierUpdateAPIView.as_view(), name='update_suppliers'),
    path('update_contact/<int:pk>/', ContactUpdateAPIView.as_view(), name='update_contact'),
    path('update_product/<int:pk>/', ProductUpdateAPIView.as_view(), name='update_product'),
    path('destroy_suppliers/<int:pk>/', SupplierDestroyAPIView.as_view(), name='destroy_suppliers'),
    path('list_suppliers/', SupplierListAPIView.as_view(), name='list_suppliers'),
]
