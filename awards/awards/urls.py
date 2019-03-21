from django.conf.urls import url
from django.contrib import admin
from myapp import views

from myapp.views import home, login_view, register_view


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name = 'home'),
    url(r'^accounts/login/', views.login_view),
    url(r'^accounts/register/', views.register_view),
    url(r'^logout/', views.logout,{'next_page':'/'}, name='logout'),
]
