from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.fazer_login, name='login'),
    path('novo_usuario/', views.cadastro, name='cadastro'),
    path('home/', views.home, name='home'),
    path('nova_proposta/', views.cadastro_proposta, name='cadastro_proposta'),
    path('consultar_proposta/', views.consultar_proposta, name='consultar_proposta'),
]