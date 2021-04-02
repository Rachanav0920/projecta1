from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello welcome to projecta1 html</h1>")
    