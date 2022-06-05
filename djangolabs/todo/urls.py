from django.urls import  path
from .views import todo_home,task_detail,task_delete,task_edit,task_save,task_add,task_insert
app_name='todo'

urlpatterns=[
    path('home/',todo_home,name='home'),
    path('details/<int:id>',task_detail,name='details'),
    path('delete/<int:id>',task_delete,name='delete'),
    path('edit/<int:id>',task_edit,name='edit'),
    path('save/',task_save,name='save'),
    path('add/',task_add,name='add'),
    path('addtask/',task_insert,name='addtask'),





]