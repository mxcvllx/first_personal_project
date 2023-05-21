from rest_framework import generics

from common.models.category_models import Category
from common.serializers import CategorySerializers


class CategoryListApiViews(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
