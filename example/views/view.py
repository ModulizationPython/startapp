from django.http import HttpResponse
from django.http import JsonResponse


def text(request):
    """test text"""
    return HttpResponse('hello world')


def json(request):
    """test  json"""
    data = {"name": 'xiaoming', 'phone': '110', 'password': '123abc', 'pet': dict(name='wangcai', age='2', type='chaiquan')}
    return JsonResponse(data)
