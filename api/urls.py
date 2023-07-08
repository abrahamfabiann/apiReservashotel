from django.urls import path,include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'customers',views.CustomerViewSet)
router.register(r'payment-methods',views.PaymentMethodViewSet)
router.register(r'room-types',views.RoomTypeViewSet)
router.register(r'rooms',views.RoomViewSet)
router.register(r'reservations',views.ReservationViewSet)

urlpatterns = [
    path('',include(router.urls))
]