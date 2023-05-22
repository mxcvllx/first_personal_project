from rest_framework import serializers

from common.models.category_models import Category


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'position', 'children']
