from audioop import reverse
from pprint import pprint
from urllib import response
from django import views
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render,HttpResponse
from django.urls import reverse 
tasks=[
    {'id':1,'name':'play footbal' ,'duration':"2", 'place':'playground', 'Priority':2},
    {'id':2,'name':'breackfast' ,'duration':"1", 'place':'kitchen', 'Priority':1},
    {'id':3,'name':'studying' ,'duration':"2", 'place':'studying room', 'Priority':3},
    {'id':4,'name':'playing valorant' ,'duration':"2", 'place':'gaming room', 'Priority':5},
    {'id':5,'name':'sleeping' ,'duration':"4", 'place':'sleeping room', 'Priority':7}

]

def todo_home(request):
    return (render (request,'todo/todo.html',context={'tasks':tasks}))
    

def task_detail(request,**arg):
    for task in tasks:
        if(task['id']==int(arg.get('id'))):
            return( render(request,'todo/task_detail.html',context={'task':task}))
        
def task_delete(request,**arg):
    for i in range(len(tasks)):
        if(tasks[i]['id']==int(arg.get('id'))):
            del tasks[i]
            break
    return HttpResponseRedirect (reverse('todo:home'))

def task_edit(request,**arg):
      for task in tasks:
        if(task['id']==int(arg.get('id'))):
            return( render(request,'todo/task_edit.html',context={'task':task}))
def task_save(request):
    new_task=request.GET
    for i in range(len(tasks)):
        if(tasks[i]['id']==int(new_task['id'])):
            tasks[i]['id']=int(new_task['id'])
            tasks[i]['name']=new_task['name']
            tasks[i]['place']=new_task['place']
            tasks[i]['duration']=int(new_task['duration'])
            tasks[i]['Priority']=int(new_task['Priority'])
            break
    return HttpResponseRedirect (reverse('todo:home'))

def task_add(request):
        return( render(request,'todo/task_add.html'))

def task_insert(request):
    new_task=request.GET
    task={}
   
    task['id']=int(new_task['id'])
    task['name']=new_task['name']
    task['place']=new_task['place']
    task['duration']=int(new_task['duration'])
    task['Priority']=int(new_task['Priority'])
    tasks.append(task)
    return HttpResponseRedirect (reverse('todo:home'))






            