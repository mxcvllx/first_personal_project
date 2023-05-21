from rest_framework import serializers

from common.models import category_models


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = category_models
        fields = ['id', 'name', 'description', 'position', 'children']
