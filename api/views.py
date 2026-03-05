from rest_framework.viewsets import ModelViewSet
from .models import Product, User
from .serializers import ProductSerializer, UserSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
