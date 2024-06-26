from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils import timezone
import uuid
import datetime


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    short_description = models.CharField(max_length=255, default='')
    long_description = models.TextField(default='', blank=True)
    fineness = models.CharField(max_length=3, default='', blank=True)
    metal = models.CharField(max_length=15, default='', blank=True)
    image = models.ImageField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class ProductReview(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    review_text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('product', 'user')


class OrderProduct(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='order_products')
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product.name} - Order #{self.order.id}"

class Order(models.Model):
    class OrderStatus(models.TextChoices):
        PAID = "P", _("Paid")
        REALIZATION = "R", _("In realization")  
        SENT = "S", _("Sent")

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, db_index=True, editable=False)
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="orders")
    products = models.ManyToManyField(Product, related_name="orders", through='OrderProduct')
    city = models.CharField(max_length=512)
    zipCode = models.CharField(max_length=64)
    street = models.CharField(max_length=128)
    houseNumber = models.CharField(max_length=64)
    status = models.CharField(max_length=1, choices=OrderStatus.choices, default=OrderStatus.PAID)
    created_at = models.DateTimeField(default=timezone.now)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Order #{self.pk} - {self.user.username} - {self.created_at}"
