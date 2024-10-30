
from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('News.urls'))
] + debug_toolbar_urls()

if settings.DEBUG:
    import debug_toolbar
    #urlpatterns = [
        # path('__debug__', include('debug_toolbar.urls'))
    # ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
