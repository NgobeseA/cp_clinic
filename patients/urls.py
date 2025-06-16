from django.urls import path
from .views import index, sign_in_view, sign_up


urlpatterns = [
    path('', index, name='home'),
    path('signup/', sign_up, name='signup'),
    path('login/', sign_in_view, name="login")
]