from django.urls import path
from chats.views import create,ls,details,tpl,delete,update

urlpatterns = [
    path('create/', create, name='create'),
    path('list/', ls, name='list'),
    path('details/', details, name='details'),
    path('hello/', tpl, name='hello'),
    path('delete/', delete, name='delete'),
    path('update/',update,name='update'),
]
