from django.conf.urls import url
from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render
import requests
import json

# Create your views here.
def home(request):
    return render(request, 'home.html')

def get(request):
    data = requests.get('http://127.0.0.1:4000/podcasts')
    podcasts = json.loads(data.text)
    data = {
        'podcasts': podcasts
    }
    print(podcasts)
    return render(request, 'get.html', data)

def post(request):
    message = {
        "Message": ''
    }
    if request.method == 'POST':
        print(request.POST['name'])
        data = {
            'nombre': request.POST['name'],
            'conductores': request.POST['conductor'],
            'last_chapter': request.POST['chapter']
        }
        data_str = json.dumps(data)
        response = requests.post('http://127.0.0.1:4000/add_podcast', data_str)
        message['Message'] = response.text        
    return render(request, 'post.html', message)

def put(request):
    message = {
        "Message": ''
    }
    if request.method == 'POST':
        id = request.POST['id']
        data = {            
            'url': request.POST['chapter']
        }
        data_str = json.dumps(data)        
        response = requests.put(f'http://127.0.0.1:4000/podcasts/{id}', data_str)
        message['Message'] = response.text        
    return render(request, 'put.html', message)

def delete(request):
    message = {
        "Message": ''
    }
    if request.method == 'POST':
        id = request.POST['id']        
        response = requests.delete(f'http://127.0.0.1:4000/delete_podcast/{id}')
        message['Message'] = response.text        
    return render(request, 'delete.html', message)