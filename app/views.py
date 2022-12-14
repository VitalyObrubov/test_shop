import os
from django.shortcuts import render
from django.db.models import Q

# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView
from app.models import Product, Status
from .serializers import ProductSerializer
@api_view(['GET'])
def products(request):
    if request.method == 'GET':
        prods = None
        if request.query_params.get('filter_status'):
            status_name = request.query_params.get('filter_status')
            status = Status.objects.filter(name = status_name).first()
            if status:
                prods = Product.objects.filter(status = status)
        elif request.query_params.get('search'):
            search_str = request.query_params.get('search')
            q = Q(title__icontains = search_str)|Q(sku__icontains = search_str)
            prods = Product.objects.filter(q).distinct()
        else:
            prods = Product.objects.all()
        serializer = ProductSerializer(prods, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def product_detail(request, pk:int):
    if request.method == 'GET':
        prod = Product.objects.filter(pk = pk).first()
        serializer = ProductSerializer(prod)

    return Response(serializer.data)

