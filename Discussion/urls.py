from rest_framework.routers import DefaultRouter
from .views import CRUD_Discussion

router = DefaultRouter()
router.register("discussions", CRUD_Discussion)

urlpatterns = router.urls