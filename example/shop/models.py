from django.contrib.auth.models import AbstractUser
from django.db import models

from salesman_stripe.models import StripeCustomerMixin


class User(StripeCustomerMixin, AbstractUser):
    """
    Custom `AUTH_USER_MODEL` to add Stripe customer id field via `StripeCustomerMixin`.
    """


class Product(models.Model):
    name = models.CharField(max_length=128)
    code = models.SlugField()
    price = models.DecimalField(max_digits=18, decimal_places=2)

    def __str__(self):
        return self.name

    def get_price(self, request):
        return self.price
