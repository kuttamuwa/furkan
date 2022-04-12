from django.urls import path, include

from runproc.views.api import run_procedure
from runproc.views.routers import router

urlpatterns = [
    path('api/', include(router.urls)),
    path('', run_procedure)
]