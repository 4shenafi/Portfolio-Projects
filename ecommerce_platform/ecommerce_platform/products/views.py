from django.shortcuts import render
from .serializers import AddProductSerializer, GetProductSerializer
from .models import AddProduct, GetProduct
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def add_product(request):
    if request.method == 'POST':
        serializer = AddProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Product added successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'error': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    else:
        return render(request, 'pages/add_product.html')