from django.urls import path
from . import views

urlpatterns = [
    path('sync/', views.sync_with_wiremock, name='sync_with_wiremock'),
]