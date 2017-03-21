from django.conf.urls import url 

from .views import user_signup, login, LoginSignup, user_logout, user_login

urlpatterns= [
url(r'demo/$', LoginSignup.as_view(), name='login_signup'),
    url(r'signup/$', user_signup, name='user-signup'),
    url(r'user_login/$', user_login, name='user_login'),
    url(r'logout/$', user_logout, name='user-logout'),
    url(r'login', login, name='login'),
]