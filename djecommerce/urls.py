from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.utils.translation import ugettext_lazy as _
# from django.contrib.authimport views as auth_views 

# from material.admin.sites import site
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

    # path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    # path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    # path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    # path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
