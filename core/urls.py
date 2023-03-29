
from django.contrib import admin
from django.urls import path
from api.views import add

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/',add),
]
