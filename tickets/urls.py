from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.ticket_list, name='ticket_list'),
    path('create/', views.create_ticket, name='create_ticket'),
    path('edit/<int:id>/', views.edit_ticket, name='edit_ticket'),
    path('delete/<int:id>/', views.delete_ticket, name='delete_ticket'),
    path('ticket/<int:id>/', views.detail_ticket, name='details_ticket'),

    # your login
    path('login/', auth_views.LoginView.as_view(template_name='tickets/login.html'), name='login'),

    # override django default login
    path('accounts/login/', auth_views.LoginView.as_view(template_name='tickets/login.html')),

    path('custom_logout/', views.logout_view, name='custom_logout'),

    # path(
    # "accounts/logout/",
    # auth_views.LogoutView.as_view(next_page="login"),
    # ),
    
]

