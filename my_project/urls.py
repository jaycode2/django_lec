from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mysite/', include('mysite.urls')),
    path('', include('pages.urls')),
    path('accounts/', include('accounts.urls')),
]
