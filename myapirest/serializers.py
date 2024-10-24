from rest_framework import serializers
from .models import Indices

class IndicesSerializer(serializers.ModelSerializer):
    class Meta:
       model = Indices
       fields = ('id','Nombre', 'Ticker', 'Country', 'Valor', 'Fecha_Actual')
       ready_only_fields = ('Fecha_Actual', )