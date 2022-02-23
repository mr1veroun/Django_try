from django.template.defaulttags import url
from django.urls import path,include
from  . import  views
from .views import ProfilePage, RegisterView
from .views import LoginView
urlpatterns = [
    path('about-us/',views.about,name ='about'),
    ##path('auth/',include('djoser.urls')),
    ##path('auth/', include('djoser.urls.authtoken')),
    ##path('auth/', include('djoser.urls.jwt')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', ProfilePage.as_view(), name="profile"),
    path(r'^accounts/register/$', RegisterView.as_view(), name="register"),
    path('accounts/login/', LoginView.as_view(), name="login"),
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

]