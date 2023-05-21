from rest_framework import serializers

from common.models import contact_us_models


class ContactUsListSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False)

    class Meta:
        model = contact_us_models
        fields = ['id', 'country', 'city', 'street', 'location', 'email', 'phone']