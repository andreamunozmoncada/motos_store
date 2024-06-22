from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'moto', MotoViewSet)
router.register(r'marca', MarcaViewSet)
router.register(r'moto_marca', moto_marcaViewSet)

urlpatterns =[
    path("api/v1/", include(router.urls))
]