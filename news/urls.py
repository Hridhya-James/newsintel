from django.contrib import admin
from django.urls import path
from newsapp import views
from django.conf import settings
from django.conf.urls.static import static
from newsapp.views import AdminDashboardView, AdminNewsView, AdminUsersView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('admin/news/', AdminNewsView.as_view(), name='admin_news'),
    path('admin/users/', AdminUsersView.as_view(), name='admin_users'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.login_view, name='login'),  # Now '/' directly serves the home page
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)