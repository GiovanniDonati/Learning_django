from django.contrib import admin
from django.urls import include, path
from .views import horario_atual, form_client, form_ok

urlpatterns = {
    path('hour', horario_atual),
    path('form', form_client),
    path('page_ok', form_ok)
}