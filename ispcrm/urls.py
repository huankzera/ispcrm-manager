from django.contrib import admin
from django.urls import path
from core.views import dashboard  # Importe a view que acabamos de criar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),  # Caminho vazio '' significa a página inicial
]