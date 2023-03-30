
from django.contrib import admin
from django.urls import path
from api.views import add,delete_task,index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/',add),
    path('delete/',delete_task),
    path('', index),
]
