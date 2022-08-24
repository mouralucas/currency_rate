from django.db import models


# Create your models here.
class CurrencyRates(models.Model):
    date = models.DateField()
    base_currency = models.CharField(max_length=5)
    currency = models.CharField(max_length=5)
    price = models.DecimalField(max_digits=20, decimal_places=10)

    class Meta:
        db_table = 'currency_rates'
