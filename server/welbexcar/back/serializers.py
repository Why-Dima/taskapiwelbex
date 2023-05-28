from rest_framework import serializers
from .models import Car, Cargo


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ['number', 'carrying_capacity', 'zip', 'location']


class CargoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cargo
        fields = ['loc_pick_up', 'loc_delivery', 'zip', 'weight', 'description']

