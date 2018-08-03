from django.conf.urls import url,include
from . import views

urlpatterns = [
    url('^offline/home/$',views.home,name='home'),
    url('^offline/message/$',views.message,name='message'),
]
