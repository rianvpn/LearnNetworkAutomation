from django.shortcuts import render, HttpResponse

def hello_world(request):
    return HttpResponse("<h1>Selamat datang</h1>")
def page1(request):
    return render(request, "page1.html")
def page2(request):
    return HttpResponse("<h1>Ini adalah Page2</h1>")