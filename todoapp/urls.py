
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('addtodo/', views.addtodo, name='addtodo'),
    path('completed/<list_id>/', views.completedtodo, name='completedtodo'),
    path('uncompleted/<list_id>/', views.uncompletedtodo, name='uncompletedtodo'),
    path('view/<list_id>/', views.viewtodo, name='viewtodo'),
    path('update/<list_id>/', views.updatetodo, name='updatetodo'),
    path('delete/<list_id>/', views.deletetodo, name='deletetodo'),
    path('login/', views.loginpage, name='loginpage'),
    path('signup/', views.signuppage, name='signuppage'),
    path('logout/', views.logoutuser, name='logoutuser'),
]
