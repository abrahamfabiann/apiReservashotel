from rest_framework import serializers
from .models import Customer
from .models import PaymentMethod
from .models import RoomType
from .models import Room
from .models import Reservation

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        #fields = ('identificationDocument','firstname','lastname','phone','email')
        fields = '__all__'
        

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'

class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'