from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.utils.translation import ugettext_lazy as _
from material.admin.sites import site
# from .core import views as core_views

admin.site.site_header = _('Eco World US')
admin.site.site_title = _('eco world us')
# site.favicon


urlpatterns = [
    # path('jet/', include('jet.urls', 'jet')),
    # path('markdown/', include( 'django_markdown.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    # path('accounts/signup/', views.signup, name='signup'),
    path('', include('core.urls', namespace='core')),
    # path('markdown/', include( 'django_markdown.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
