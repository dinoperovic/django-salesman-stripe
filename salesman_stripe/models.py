from django.db import models


class StripeCustomerMixin(models.Model):
    """
    Abstract model that enables saving Stripe customer ID relation to the User model.

    To enable this feature your custom `AUTH_USER_MODEL` should inherit from this class
    or implement the `stripe_customer_id` field itself.

    You can further control where the Stripe customer ID is stored for the User
    by overriding the `get_stripe_customer_id` and `save_stripe_customer_id`
    methods in the `salesman_stripe.payment.StripePayment` class.
    """

    stripe_customer_id = models.CharField(max_length=128, null=True, editable=False)

    class Meta:
        abstract = True
