from rest_framework import routers

from Weekend.views import *

router = routers.DefaultRouter()
router.register(r'user-file', UserViewSet, basename='user-file')
urlpatterns = router.urls
