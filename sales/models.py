from django.db import models
from products.models import Products
from customers.models import Customer
from profiles.models import Profile
from django.utils import timezone

class Position(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField()
    price = models.FloatField(blank=True)
    created = models.DateTimeField(blank=True)

    def save(self, args, **kwargs):
        self.price = self.product.price * self.quantity
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"id: {self.id}, product: {self.product.name}"

class Sale(models.Model):
    transcation_id = models.CharField(max_length=255, blank=True)
    positions = models.ManyToManyField(Position)
    total_price = models.FloatField(blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    salesman = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.total_price

    def save(self, *args, **kwargs):
        if self.transcation_id == "":
            self.transcation_id == ''
        if self.created_at is None:
            self.created_at = timezone.now()
        return super().save(*args, **kwargs)

    def get_positions(self):
        return self.positions.all()

class CSV(models.Model):
    pass