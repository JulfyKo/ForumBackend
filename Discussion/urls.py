from rest_framework.routers import DefaultRouter
from .views import CRUD_Discussion, CRUD_Comment

router = DefaultRouter()
router.register("discussions", CRUD_Discussion)
router.register("comments", CRUD_Comment )

urlpatterns = router.urls