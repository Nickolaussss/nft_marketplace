from django.urls import path

from pages import views

app_name = 'pages'


urlpatterns = [
    path('marketplace/', views.marketplace, name='marketplace'),
    path('rankings/', views.rankings, name='rankings'),
    path('connect-a-wallet/', views.connect_a_wallet, name='connect_a_wallet'),
]
