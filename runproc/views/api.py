from django.db import connections
from rest_framework import filters
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.renderers import AdminRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from runproc.models.models import TestTable
from runproc.models.serializers import TestTableSerializer
from config import settings

db_con = connections['default']  # normalde boyle raw kullanmak guzel bi sey degil.
sp_raw = settings.SP['run_sql']  # configten çekelim


# class based view. Genellikle model ile birlikte kullanilir.
# model ile kullanmazken de APIView ile kullanabilirsin.
class TestTableAPI(ModelViewSet):
    queryset = TestTable
    serializer_class = TestTableSerializer
    permission_classes = [
        # buradan acilirsin.
        # IsAuthenticated,
        # IsAdminUser
    ]
    filter_backends = [
        # filters.SearchFilter
    ]
    renderer_classes = [
        # pretty useful
        AdminRenderer,
        JSONRenderer
    ]

    search_fields = ['created_date', 'description']
    ordering = 'created_date'

    # crud operations
    def create(self, request, *args, **kwargs):
        return super(TestTableAPI, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(TestTableAPI, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(TestTableAPI, self).destroy(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(TestTableAPI, self).list(request, *args, **kwargs)


@api_view()
def run_procedure(request):
    cursor = db_con.cursor()
    result = cursor.execute(sp_raw)

    return Response({
        "message": "Task is completed !",
        "result": result
    })

