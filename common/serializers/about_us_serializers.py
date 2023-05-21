from rest_framework import serializers

from common.models import about_us_models


class AboutUsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False)

    class Meta:
        model = about_us_models
        fields = ['id', 'title', 'description', 'image']
