
from django.conf.urls import url, include
from .views import *


urlpatterns = [
     # URL for restless API
     url(r'^users/get/', include(UserResourse.urls())),
     url(r'^posts/get/', include(PostResourse.urls())),

     #URL for views form for working with API
     #You can connect to URL /api/v.2/reg/  and create new customer in HTML form"""
     url(r'^reg/', reg),
     url(r'^post/', post_),
     url(r'^users/del/',delete),
     url(r'^posts/del/', delete_p),
     url(r'^users/update/', put),
     url(r'^posts/update/', put_post),
]

