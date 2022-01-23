from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.home, name='home'),
    path('', user_views.home, name='home'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/home.html'), name='logout'),

    path('vegetable/', user_views.vegetable, name='vegetables'),
    path('veg_detail/<int:pk>', user_views.veg_detail, name='veg_detail'),

    path('fruit/', user_views.fruit, name='fruit'),
    path('fruit_detail/<int:pk>', user_views.fruit_detail, name='fruit_detail'),

    path('beverage/', user_views.beverage, name='beverage'),
    path('beverage_detail/<int:pk>', user_views.beverage_detail, name='beverage_detail'),

    path('baby/', user_views.baby, name='baby'),
    path('baby_detail/<int:pk>', user_views.baby_detail, name='baby_detail'),

    path('bread/', user_views.bread, name='bread'),
    path('bread_detail/<int:pk>', user_views.bread_detail, name='bread_detail'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)