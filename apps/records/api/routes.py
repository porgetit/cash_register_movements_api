from rest_framework.routers import DefaultRouter
from apps.records.api.views.general_views import RecordViewSet

router = DefaultRouter()
router.register(r'records', RecordViewSet, basename= 'records')

urlpatterns = router.urls