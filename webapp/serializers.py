from django.contrib.auth.models import User
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from .models import CarModel, Car, Price, Mileage, Quantity, Equipment


class CarModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarModel
        fields = ('brand', 'model', 'gen')


class MileageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mileage
        fields = ('car_mileage', )


class QuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Quantity
        fields = ('car_quantity', )


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ('body', 'transmission', 'engine', 'color')


class PriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Price
        fields = ('car_price', )


class CarSerializer(WritableNestedModelSerializer,
                    serializers.ModelSerializer):
    car_model = CarModelSerializer()
    equipment = EquipmentSerializer(many=True)
    price = PriceSerializer()
    mileage = MileageSerializer(many=True)
    quantity = QuantitySerializer()

    class Meta:
        model = Car
        fields = ('id', 'car_model', 'equipment', 'price', 'mileage', 'quantity', )


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password', )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
