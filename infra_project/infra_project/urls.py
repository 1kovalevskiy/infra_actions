from django.contrib import admin
from django.urls import path, include  # noqa


urlpatterns = [
    path('', include('infra_app.urls', namespace='infra_app')),
    path('admin/', admin.site.urls),
]
