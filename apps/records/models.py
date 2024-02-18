from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Record(models.Model):
    LIST_RECORDS_TYPES = (
        (1, 'Ingreso'),
        (2, 'Egreso'),
    )

    date_created = models.DateTimeField(
        'Fecha de creación',
        auto_now = False,
        auto_now_add = True,
        null = True,
    )

    product_name = models.CharField(
        'Nombre de producto',
        max_length = 250,
        null = False,
        blank = False,
    )

    product_amount = models.PositiveIntegerField(
        'Cantidad',
        default = 1,
    )

    monetary_amount = models.DecimalField(
        'Monto',
        decimal_places = 2,
        max_digits = 10,
    )

    record_type = models.PositiveIntegerField(
        'Tipo de registro',
        default = 1,
        choices = LIST_RECORDS_TYPES,
    )

    creator = models.ForeignKey(
        User,
        on_delete = models.SET_NULL,
        null = True,
        blank =  True,
    )

    class Meta:
        verbose_name = 'Record'
        verbose_name_plural = 'Records'
        
    def __str__(self) -> str:
        return f'{self.date_created} - {self.product_name}'

