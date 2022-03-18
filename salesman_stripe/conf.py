from __future__ import annotations

from typing import Any, Optional


class AppSettings:
    @property
    def SALESMAN_STRIPE_SECRET_KEY(self) -> str:
        """
        Stripe API secret key.
        """
        return self._required_setting('SALESMAN_STRIPE_SECRET_KEY')

    @property
    def SALESMAN_STRIPE_WEBHOOK_SECRET(self) -> str:
        """
        Stripe webhook secret.
        """
        return self._required_setting('SALESMAN_STRIPE_WEBHOOK_SECRET')

    @property
    def SALESMAN_STRIPE_PAYMENT_LABEL(self) -> str:
        """
        Payment method label used when displayed in the basket.
        """
        return self._setting('SALESMAN_STRIPE_DEFAULT_CURRENCY', 'Pay with Stripe')

    @property
    def SALESMAN_STRIPE_DEFAULT_CURRENCY(self) -> str:
        """
        Default ISO currency used for payments, must be set to a valid Stripe currency.
        https://stripe.com/docs/currencies
        """
        return self._setting('SALESMAN_STRIPE_DEFAULT_CURRENCY', 'USD')

    @property
    def SALESMAN_STRIPE_CANCEL_URL(self) -> Optional[str]:
        """
        URL to redirect to when Stripe payment is cancelled.
        """
        return self._setting('SALESMAN_STRIPE_CANCEL_URL')

    @property
    def SALESMAN_STRIPE_SUCCESS_URL(self) -> Optional[str]:
        """
        URL to redirect to when Stripe payment is successfull.
        """
        return self._setting('SALESMAN_STRIPE_SUCCESS_URL')

    @property
    def SALESMAN_STRIPE_PAID_STATUS(self) -> str:
        """
        Default paid status for fullfiled orders.
        """
        return self._setting('SALESMAN_STRIPE_PAID_STATUS', 'PROCESSING')

    def _setting(self, name: str, default: Any = None) -> Any:
        from django.conf import settings

        return getattr(settings, name, default)

    def _required_setting(self, name: str) -> Any:
        value = self._setting(name)
        if not value:
            self._error(f"Missing `{name}` in your settings.")
        return value

    def _error(self, message: str | Exception) -> None:
        from django.core.exceptions import ImproperlyConfigured

        raise ImproperlyConfigured(message)


app_settings = AppSettings()
