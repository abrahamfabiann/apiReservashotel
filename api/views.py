from rest_framework import viewsets
from .serializer import CustomerSerializer
from .serializer import PaymentMethodSerializer
from .serializer import RoomTypeSerializer
from .serializer import RoomSerializer
from .serializer import ReservationSerializer
from .models import Customer
from .models import PaymentMethod
from .models import RoomType
from .models import Room
from .models import Reservation

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class PaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer

class RoomTypeViewSet(viewsets.ModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer