from django.conf.urls import url,include
from . import views

urlpatterns = [
    url('^home/$',views.home,name='home'),
    url('^message/$',views.message,name='message'),
    url('^all_message/$',(views.all_message).as_view(),name='all_message'),
    url('^save_user/$',(views.save_user).as_view(),name='save_user'),
    url('^show_all/$',(views.all_user).as_view(),name='all_user'),
    url('^show_detail/$',(views.show_details).as_view(),name='show_detail'),
    url('^notify_user/$',(views.notify_user).as_view(),name='notify'),
    url('^save_message/$',(views.save_message).as_view(),name='save_message'),
]
