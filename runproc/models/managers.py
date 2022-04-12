from django.db import models

# burada asil tabloyu çağıramazsın. bkz. diamond import problem


class TestTableManager(models.Manager):
    def check_some_processes(self):
        """
        Burayi kafana gore doldurabilirsin. Olayı şu: ORM'den çağırdığın modele yaptırmak istediğin işler.
        Örneğin create, filter, update vs. metotları burada ezebilirsin.
        Default: models.manager kullanılır. Sen istersen ikisini birden de kullanabilirsin
        :return:
        """
        print("Do some")
