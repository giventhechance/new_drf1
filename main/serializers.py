from rest_framework import serializers

from main.models import Product, Service


class ProdSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=128)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    description = serializers.CharField(max_length=255)
    product_set = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)


class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=128)
    description = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    category = CategorySerializer()


class ProductPOSTSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=128)
    description = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    category_id = serializers.IntegerField()


class CategoryServSerializer(serializers.Serializer):
    name = serializers.CharField()
    slug = serializers.SlugField()


class ServiceSerializerForSalon(serializers.Serializer):
    title = serializers.CharField()
    slug = serializers.SlugField()
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    category = CategoryServSerializer()


class SalonSerializer(serializers.Serializer):
    name = serializers.CharField()
    slug = serializers.SlugField()
    # service_set = ServiceSerializerForSalon(many=True)


class ServiceSerializer(serializers.Serializer):
    title = serializers.CharField()
    slug = serializers.SlugField()
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    category = CategoryServSerializer()
    salons = SalonSerializer(many=True)



class AutoSerializer(serializers.Serializer):
    brand = serializers.CharField(max_length=255)
    model = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)


class ServiceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'



