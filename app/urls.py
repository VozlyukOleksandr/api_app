
from django.conf.urls import url, include
from .views import *


urlpatterns = [

     url(r'^users/get/(?P<uk>[0-9]+)/', include(UserResourse.urls())),
     url(r'^users/get/', include(UserResourse.urls())),

     url(r'^posts/get/', PostResourse.as_list(), name='api_post_list'),
     url(r'^posts/get/(?P<pk>[0-9]+)/', include(PostResourse.urls())),

]


"""API должно иметь возможность создавать, удалять, редактировать и выводить записи по 2 моделям. 
+ Базовая фильтрация по полям будет плюсом."""
