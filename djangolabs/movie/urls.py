from django.urls import  URLPattern, path
from .views import movie_delete, movie_details, movie_home,movie_create, movie_update
app_name='movie'

urlpatterns=[
    path('home/',movie_home,name='home'),
    path('create/',movie_create,name='create'),
    path('details/<int:id>',movie_details,name='details'),
    path('delete/<int:id>',movie_delete,name='delete'),
    path('update/<int:id>',movie_update,name='update')
]