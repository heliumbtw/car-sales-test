from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class CarModel(models.Model):
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=50)
    gen = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.brand} {self.model} Gen {self.gen}'

    class Meta:
        verbose_name_plural = 'Car Model'


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='car_model')

    def __str__(self):
        return f"id {self.id}"

    class Meta:
        verbose_name_plural = 'Car'


class Price(models.Model):
    price = models.OneToOneField(Car, on_delete=models.CASCADE, related_name='price', null=True)
    car_price = models.IntegerField()

    def __str__(self):
        return f"{self.car_price} $"

    class Meta:
        verbose_name_plural = 'Price'


class Mileage(models.Model):
    mileage = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='mileage', null=True)
    car_mileage = models.IntegerField()

    def __str__(self):
        return f"{self.car_mileage} km"

    class Meta:
        verbose_name_plural = 'Mileage'


class Quantity(models.Model):
    quantity = models.OneToOneField(Car, on_delete=models.CASCADE, related_name='quantity', null=True)
    car_quantity = models.IntegerField()

    def __str__(self):
        return f"{self.car_quantity}"

    class Meta:
        verbose_name_plural = 'Quantity'


class Equipment(models.Model):
    equipment = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='equipment', null=True)
    body = models.CharField(max_length=30)
    transmission = models.CharField(max_length=30)
    engine = models.CharField(max_length=30)
    color = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.body}, {self.transmission}, {self.engine}, {self.color}'

    class Meta:
        verbose_name_plural = 'Equipment'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
