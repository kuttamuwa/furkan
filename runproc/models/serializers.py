from rest_framework.serializers import ModelSerializer

from runproc.models.models import TestTable


class TestTableSerializer(ModelSerializer):
    # istersen ayri ayri da yazabilirsin tabii
    class Meta:
        model = TestTable
        fields = '__all__'
