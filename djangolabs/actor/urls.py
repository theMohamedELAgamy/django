from django.urls import  URLPattern, path
from .views import actor_home,actor_details,actor_delete,actor_create,actor_update
app_name='actor'

urlpatterns=[
   path('home/',actor_home,name='home'),
   path('details/<int:id>',actor_details,name='details'),
   path('delete/<int:id>',actor_delete,name='delete'),
   path('create/',actor_create,name='create'),
   path('update/<int:id>',actor_update,name='update'),

   
]