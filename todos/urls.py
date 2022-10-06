from .views import TodoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('todos', TodoViewSet, basename='todo')
urlpatterns = router.urls