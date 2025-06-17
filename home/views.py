from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("<center><h1>Hello, World from Django on Vercel!</h1></center>")
