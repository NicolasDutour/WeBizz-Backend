from rest_framework import routers
from user import views

router = routers.DefaultRouter()
router.register('api/users', views.UserViewSet, 'user')

urlpatterns = router.urls
