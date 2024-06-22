from rest_framework import viewsets, permissions
from .models import *
from .serializer import *
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class MotoViewSet(viewsets.ModelViewSet):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()
    serializer_class = MotoSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission()for permission in permission_classes]

        
    

class MarcaViewSet(viewsets.ModelViewSet):
    serializer_class = MarcaSerializer
    queryset = Marca.objects.all()

class moto_marcaViewSet(viewsets.ModelViewSet):
    serializer_class = moto_marcaSerializer
    queryset = moto_marca.objects.all()



