from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from notes.views import note_list_view, finish_item
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', note_list_view, name='note-list'),
    path('finish-list/<id>/', finish_item, name='finish-item')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    