from rest_framework import routers

from runproc.views.api import TestTableAPI

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'test', TestTableAPI)
