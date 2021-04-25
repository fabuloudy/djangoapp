from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from chats.models import Chat
from chats.models import User
from django.forms.models import model_to_dict

def chat_to_dict(chat):
    return { 
        'id': chat.id, 
        'chatType': chat.chatType, 
        'user1.name': chat.user1.name, 
        'user2.name': chat.user2.name,
    }



db = [{'id':1,'name':'Yulia','type':'single'},
      {'id':2,'name':'PYBACKEND','type':'group'}]

@require_http_methods(["GET"])
def ls(request):
    return JsonResponse({'body': [chat_to_dict(c) for c in Chat.objects.all()]})

@csrf_exempt
@require_http_methods(["POST"])
def create(request):
    user1 = User.objects.get(id=int(request.POST['user1']))
    user2 = User.objects.get(id=int(request.POST['user2']))
    new_chat = Chat(chatType=request.POST['chatType'],user1=user1,user2=user2)
    new_chat.save()
    return JsonResponse({'body': 'chat created: {}'.format(chat_to_dict(new_chat))})

@require_http_methods(["GET"])
def details(request):
    chat = Chat.objects.get(id=int(request.GET['id']))
    return JsonResponse({'body': chat_to_dict(chat)})

@require_http_methods(["GET"])
def tpl(request):
    with open('templates/index.html', 'r') as f:
        return HttpResponse(f.read())
    return JsonResponse({'status':'Error loading template'})
         
@csrf_exempt
@require_http_methods(["POST"])
def delete(request):
    chat = Chat.objects.get(id=int(request.POST['id']))
    chat.delete()
    return JsonResponse({'status': 'deleted'})
         
@csrf_exempt
@require_http_methods(["POST"])
def update(request):
    chat = Chat.objects.get(id=int(request.POST['id']))
    chat.chatType=request.POST['chatType']
    chat.save()
    return JsonResponse({'status': 'updated'})



