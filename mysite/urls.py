from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('TODO/', include('TODO.urls')),
    path('admin/', admin.site.urls),
]