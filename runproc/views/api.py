from django.db import connections
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import filters
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.renderers import AdminRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from runproc.forms.SPForm import SPForm
from runproc.models.models import TestTable
from runproc.models.serializers import TestTableSerializer
from config import settings

db_con = connections['default']  # normalde boyle raw kullanmak guzel bi sey degil.
sp_raw = settings.SP['run_sql']  # configten çekelim


# class based view. Genellikle model ile birlikte kullanilir.
# model ile kullanmazken de APIView ile kullanabilirsin.
class TestTableAPI(ModelViewSet):
    queryset = TestTable.objects.all()
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


def run_procedure(request):
    if request.method == 'POST':
        form = SPForm(request.POST)
        if form.is_valid():
            # cursor = db_con.cursor()
            # result = cursor.execute(sp_raw)
            return HttpResponse("<h1> Thanks </h1>", status=200)

    else:
        form = SPForm()

        return render(request, 'runproc/dugmeli.html', {'form': form})