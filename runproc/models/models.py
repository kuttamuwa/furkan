from django.db import models
from runproc.models.managers import TestTableManager


class TestTable(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(null=True, max_length=250)

    operator_manager = TestTableManager()
    objects = models.Manager()  # yazmana gerek yok ben gör diye ekledim.

    def __str__(self):
        return f"Test tablosu : \n" \
               f"Tarih: {self.created_date} - Tanım : {self.description}"

    class Meta:
        db_table = 'TEST_TABLE'
