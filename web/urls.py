from rest_framework import routers
from .api import JugueteViewSet, ContactFormViewSet

router = routers.DefaultRouter()

router.register(r'juguete', JugueteViewSet)
router.register(r'contacto', ContactFormViewSet)

urlpatterns = router.urls
