# Saleman Stripe example

This example project demo.

## Installation

Salesman uses [Poetry](https://python-poetry.org/) for virtualenv and dependency management. Make sure you have it installed first.

### Clone the repo

```bash
git clone https://github.com/dinoperovic/django-salesman-stripe.git
```

### Run the example

```bash
cd django-salesman-stripe/
poetry install
poetry run example/manage.py migrate
poetry run example/manage.py createsuperuser
poetry run example/manage.py runserver
```

**Done!** You can now:

- Add products in admin.
- Navigate to `/api/` and start adding products to the basket.
- Purchase orders using the Stripe payment method.
