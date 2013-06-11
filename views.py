from django.http import HttpResponse

def multihost1(request):
    return HttpResponse('multihost1')

def multihost2(request):
    return HttpResponse('multihost2')

def multihost3(request):
    return HttpResponse('multihost3')
