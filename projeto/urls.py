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
    path('logout/', views.fazer_logout, name='logout'),
    path('noticias/', views.noticias, name='noticias'),
    path('consultar_usuario/', views.consultar_usuario, name='consultar_usuario'),
    path('ajustar_proposta/<int:id>/', views.ajustar_proposta, name='ajustar_proposta'),
]