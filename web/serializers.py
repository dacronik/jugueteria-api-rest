from rest_framework import serializers
from .models import Juguete, ContactForm

class JugueteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juguete
        fields = ('id', 'name', 'description', 'image_url','price','slug','is_private')

class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields =('id','customer_email', 'customer_name', 'message')