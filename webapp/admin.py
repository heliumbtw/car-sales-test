from django.contrib import admin
from .models import Equipment, Mileage, Price, Quantity, Car, CarModel

admin.site.register(Equipment)
admin.site.register(Mileage)
admin.site.register(Price)
admin.site.register(Quantity)
admin.site.register(CarModel)
admin.site.register(Car)