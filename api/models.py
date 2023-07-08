from django.db import models

# Create your models here.
class Customer(models.Model):
    identification_document = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

class PaymentMethod(models.Model):
    name = models.CharField(max_length=50)

class RoomType(models.Model):
    name = models.CharField(max_length=50)

class Room(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    capacity = models.IntegerField()
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    type = models.ForeignKey(RoomType, on_delete=models.CASCADE)


class Reservation(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    amount_paid = models.DecimalField(max_digits=8, decimal_places=2)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    STATUS_CHOICES = (
        ('Pendiente', 'Pendiente'),
        ('Pagado', 'Pagado'),
        ('Eliminado', 'Eliminado'),
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)