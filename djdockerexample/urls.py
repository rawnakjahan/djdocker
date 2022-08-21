from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include

from api import views

urlpatterns = [
    path('account/', views.account_post),
    path('admin/', admin.site.urls),
]
