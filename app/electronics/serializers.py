from rest_framework import serializers
from electronics.models import Contact, Product, Supplier

class ContactSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Contact
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Product
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        exclude = ('user', )

class SupplierSerializerUpdate(serializers.ModelSerializer):
    debt = serializers.FloatField(read_only=True)
    class Meta:
        model = Supplier
        exclude = ('user', )


class SupplierSerializerCreate(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    contact = ContactSerializer()
    product = ProductSerializer()

    class Meta:
        model = Supplier
        fields = ('user', 'level', 'title', 'contact', 'product', 'chain', 'debt')

    def create(self, validated_data):
        data_contact = validated_data.pop('contact')
        new_contact = Contact.objects.create(**data_contact)
        data_product = validated_data.pop('product')
        new_product = Product.objects.create(**data_product)
        new_supplier = Supplier.objects.create(**validated_data, contact=new_contact, product=new_product)
        return new_supplier
    
