from rest_framework import serializers
from apps.records.models import Record


class RecordSerializer (serializers.ModelSerializer) :
    class Meta :
        model = Record
        fields = (
            'date_created',
            'product_name',
            'product_amount',
            'monetary_amount',
            'record_type',
            'creator',
        )
