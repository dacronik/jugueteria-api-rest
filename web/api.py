from .models import Juguete, ContactForm
from rest_framework import viewsets, permissions
from .serializers import JugueteSerializer, ContactFormSerializer 

class JugueteViewSet(viewsets.ModelViewSet):
    queryset = Juguete.objects.all()
    permission_classes =[permissions.AllowAny]
    serializer_class = JugueteSerializer

class ContactFormViewSet(viewsets.ModelViewSet):
    queryset = ContactForm.objects.all()
    permission_classes =[permissions.AllowAny]
    serializer_class = ContactFormSerializer