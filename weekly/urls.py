from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from Weekend.urls import router

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
from weekly import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/vi/', include(router.urls)),
                  path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
