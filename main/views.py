from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, Category, CategoryServ, Service, Salon, Auto
from .serializers import ProductSerializer, CategorySerializer, ProductPOSTSerializer, CategoryServSerializer, \
    ServiceSerializer, SalonSerializer, AutoSerializer, ServiceModelSerializer


@api_view(['GET', 'POST'])
def get_product(request):
    if request.method == 'POST':
        products = request.data
        print(products)
        products_serialized = ProductPOSTSerializer(data=products)
        if products_serialized.is_valid(raise_exception=True):
            print(products_serialized.validated_data)
            Product.objects.create(**products_serialized.validated_data)
        else:
            print(products_serialized.errors)

        return Response('ok')

    products = Product.objects.all()
    products_serializer = ProductSerializer(products, many=True)

    return Response(products_serializer.data)


@api_view(['GET'])
def get_category(request):
    categories = Category.objects.all()
    categories_serializer = CategorySerializer(categories, many=True)

    return Response(categories_serializer.data)


@api_view()
def get_categories(request):
    categories = CategoryServ.objects.all()
    serializers = CategoryServSerializer(categories, many=True)
    return Response(serializers.data)


@api_view()
def get_services(request):
    services = Service.objects.all()
    serializers = ServiceSerializer(services, many=True)
    return Response(serializers.data)


@api_view()
def get_services_for_title(request, text):
    service = get_object_or_404(Service, slug=text)
    serializers = ServiceSerializer(service)
    print(service)
    return Response(serializers.data)


@api_view()
def get_salons(request):
    salons = Salon.objects.all()
    serializers = SalonSerializer(salons, many=True)
    print(salons[0]._state)
    return Response(serializers.data)


@api_view(['GET'])
def get_json_autos(request):
    autos = Auto.objects.filter()
    serializers = AutoSerializer(autos, many=True)
    print(autos)
    print(serializers.data[0]['brand'])
    return Response(serializers.data)


class ServicesApiView(APIView):
    def get(self, request):
        queryset = Service.objects.all()
        serializers = ServiceSerializer(queryset, many=True)
        return Response(serializers.data)

    def post(self, request):
        data = ServiceSerializer(data=request.data)
        print(request.data)
        if data.is_valid():
            new_service = Service(
                title = data.data['title'],
                slug = data.data['slug'],
                price = data.data['price'],
                category=CategoryServ.objects.get(**data.data['category']))
            new_service.save()
            new_service.salons.add(Salon.objects.get(**data.data['salons']))

            return Response({'service': 'ok'})
        else:
            print(data.errors)

        return Response({'status': 'data is not valid'})
