from django.urls import path
from cookieless.tests.views import MyClassView, disable_cookies, enable_cookies
from cookieless.tests.views import my_function_view, my_plain_view

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()


urlpatterns = [
    # Examples views:
    path("function-view.html", my_function_view),
    path("plain-view.html", my_plain_view),
    path("index.html", MyClassView.as_view()),
    path("disable_cookies", disable_cookies),
    path("enable_cookies", enable_cookies),
    path("", MyClassView.as_view()),
    # Uncomment the next line to enable the admin:
    path("admin/", admin.site.urls),
]
