
from django.contrib import admin
from django.urls import include, path
from dashboard import views
from django.conf.urls.static import static
import os
from django.conf import settings
from django.views.generic import TemplateView
# Serve static and media files during development only
from dashboard.views import PostViewSet, serve_pdf, upload_file, fetch_documents, qc_document


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
