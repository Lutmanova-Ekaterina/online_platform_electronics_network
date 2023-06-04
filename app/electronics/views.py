from rest_framework import filters
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from electronics.models import Supplier, Contact, Product
from electronics.permissions import IsActive
from electronics.serializers import SupplierSerializerCreate, SupplierSerializer, ContactSerializer, ProductSerializer, SupplierSerializerUpdate

class SupplierCreateAPIView(CreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializerCreate
    # permission_classes = [IsAuthenticated, IsActive]


class SupplierRetrieveAPIView(RetrieveAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    # permission_classes = [IsAuthenticated, IsActive]


class SupplierListAPIView(ListAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializerCreate
    # permission_classes = [IsAuthenticated, IsActive]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['contact__city']


class SupplierUpdateAPIView(UpdateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializerUpdate
    # permission_classes = [IsAuthenticated, IsActive]


class SupplierDestroyAPIView(DestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    # permission_classes = [IsAuthenticated, IsActive]


class ContactUpdateAPIView(UpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    # permission_classes = [IsAuthenticated, IsActive]


class ProductUpdateAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticated, IsActive]

