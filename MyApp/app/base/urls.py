
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("",views.home,name="home"),
    path("register/",views.Register,name="register"),
    path("about/",views.About,name="About"),
    path("login/",LoginView.as_view(template_name="base/login.html"),name="login"),
    path("logout/",LogoutView.as_view,name="logout"),
    path('course/<int:course_id>/', views.course_detail, name='course'),
]
