from django.conf import settings
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.contrib import admin
from django.views import defaults as default_views

from django.conf.urls.i18n import i18n_patterns
#{%- if cookiecutter.use_async == 'y' %}
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#{%- endif %}
#{%- if cookiecutter.use_drf == 'y' %}
#from rest_framework.authtoken.views import obtain_auth_token
#{%- endif %}

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('upload/', views.upload, name='upload'),
    path('books/', views.book_list, name='book_list'),
    path('books/upload/', views.upload_book, name='upload_book'),
    path('books/<int:pk>/', views.delete_book, name='delete_book'),

    path('class/books/', views.BookListView.as_view(), name='class_book_list'),
    path('class/books/upload/', views.UploadBookView.as_view(), name='class_upload_book'),

    path('admin/', admin.site.urls),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
#{%- if cookiecutter.use_async == 'y' %}
#if settings.DEBUG:
    # Static file serving when using Gunicorn + Uvicorn for local web socket development
#    urlpatterns += staticfiles_urlpatterns()
#{%- endif %}
#{% if cookiecutter.use_drf == 'y' %}
# API URLS
#urlpatterns += [
    # API base url
#    path("api/", include("config.api_router")),
    # DRF auth token
#    path("auth-token/", obtain_auth_token),
#]
#{%- endif %}
if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] \
            + urlpatterns
