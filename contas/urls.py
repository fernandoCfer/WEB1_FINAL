from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.login, name='index_login'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/<usuario>', views.atualizar_dados, name='atualizar_dados'),
    path('fav/<int:id>/', views.favorito_add, name='favorito_add'),
    path('perfil/favoritos', views.favoritos_lista, name='favoritos_lista'),

    path('alterar_senha/', auth_views.PasswordResetView.as_view(template_name='contas/alterar_senha.html'), name='alterar_senha'),
    path('alterar_senha_enviado/', auth_views.PasswordResetDoneView.as_view(template_name='contas/alterar_senha_enviado.html'), name='password_reset_done'),
    path('alterar_senha/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='contas/alterar_senha_form.html'), name='password_reset_confirm'),
    path('alterar_senha_completo/', auth_views.PasswordResetCompleteView.as_view(template_name='contas/alterar_senha_completo.html'), name='password_reset_complete')
]