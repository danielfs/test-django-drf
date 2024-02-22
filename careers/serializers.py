from rest_framework import serializers

from careers.models import Career


class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = ['id', 'username', 'created_datetime', 'title', 'content']
