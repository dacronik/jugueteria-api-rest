from django.db import models

# Create your models here.
class Juguete(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField(blank=True)
    price = models.IntegerField()
    slug = models.SlugField()
    is_private = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.name

#formulario de contacto
class ContactForm(models.Model):
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()
    
    def __str__(self) -> str:
        return f'{self.customer_name} {self.customer_email}'