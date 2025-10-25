from django.urls import path
from . import views
from earnings.views import logout_user


urlpatterns = [
    path('', views.earnings_list, name='earnings_list'),
    path('add/', views.add_earning, name='add_earning'),
    path('<int:pk>/', views.earnings_detail, name='earnings_detail'),
    path('logout/', logout_user, name='logout'),
]
