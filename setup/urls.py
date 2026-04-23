from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from portal import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Esta linha abaixo faz com que se não estiver logado, vá para o login
    path('', views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='portal/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('cadastrar-estudante/', views.cadastrar_estudante, name='cadastrar_estudante'),
    path('lancar-nota/', views.lancar_nota, name='lancar_nota'),
]


