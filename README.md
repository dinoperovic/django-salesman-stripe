# Salesman Stripe

[![PyPI](https://img.shields.io/pypi/v/django-salesman-stripe)](https://pypi.org/project/django-salesman-stripe/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-salesman-stripe)](https://pypi.org/project/django-salesman-stripe/)
[![PyPI - Django Version](https://img.shields.io/pypi/djversions/django-salesman-stripe)](https://pypi.org/project/django-salesman-stripe/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[Stripe](https://stripe.com/) payment integration for [Salesman](https://github.com/dinoperovic/django-salesman).

## Installation

Install the package using pip:

```bash
pip install django-salesman-stripe
```

Add to your setting file:

```python
INSTALLED_APPS += ['salesman_stripe']
SALESMAN_PAYMENT_METHODS = ['salesman_stripe.payment.StripePayment']
SALESMAN_STRIPE_SECRET_KEY = '<stripe-secret-key>'
SALESMAN_STRIPE_WEBHOOK_SECRET = '<stripe-webhook-secret>'
```

### Local setup

To simulate webhooks while in development you can use the [Stripe CLI](https://stripe.com/docs/stripe-cli).
After you've installed the CLI, you can run:

```bash
stripe listen --forward-to localhost:8000/api/payment/stripe/webhook/
```

This will connect the webhook and output the signing secret for `SALESMAN_STRIPE_WEBHOOK_SECRET` setting.

### Additional settings

Optional additional settings that you can override:

```python
# Payment method label used when displayed in the basket.
SALESMAN_STRIPE_PAYMENT_LABEL = 'Pay with Stripe'

# Default ISO currency used for payments (https://stripe.com/docs/currencies)
SALESMAN_STRIPE_DEFAULT_CURRENCY = 'usd'

# URL to redirect to when Stripe payment is cancelled.
SALESMAN_STRIPE_CANCEL_URL = '/stripe/cancel/'

# URL to redirect to when Stripe payment is successfull.
SALESMAN_STRIPE_SUCCESS_URL = '/stripe/success/'

# Default paid status for fullfiled orders.
SALESMAN_STRIPE_PAID_STATUS = 'PROCESSING'
```

### Customer syncing

It is recommended to enable Stripe customer syncronization with your User model.
This will require an extra field on your User model which will hold the Stripe customer ID.
Easiest way to do this is to define a custom user model:

```python
# shop/models.py
from salesman_stripe.models import StripeCustomerMixin

class User(StripeCustomerMixin, AbstractUser):
    pass
```

You should then register your custom user model in `settings.py`:

```python
AUTH_USER_MODEL = 'shop.User'
```

An alternative approach would be to override the `get_stripe_customer_id` and `save_stripe_customer_id`
methods in a custom `StripePayment` class, see more in advanced usage section below.

## Advanced usage

To gain more control feel free to extend the `StripePayment` class with your custom functionality:

```python
# shop/payment.py
from salesman_stripe.payment import StripePayment
from salesman_stripe.conf import app_settings

class MyStripePayment(StripePayment):
    def get_stripe_customer_data(self, obj, request):
        # https://stripe.com/docs/api/customers/create
        data = super().get_stripe_customer_data(obj, request)
        if obj.user and obj.user.phone_number:
            data['phone'] = obj.user.phone_number
        return data

    def get_currency(self, request):
        currency = request.GET.get('currency', None)
        # Check currency is valid for Stripe...
        return currency or app_settings.SALESMAN_STRIPE_DEFAULT_CURRENCY
```

Make sure to use your payment method in `settings.py`:

```python
SALESMAN_PAYMENT_METHODS = ['shop.payment.MyStripePayment']
```

The `StripePayment` class is setup with extending in mind, feel free to explore other methods.
