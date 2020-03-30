from django.shortcuts import render, HttpResponse

def hello_world(request):
    context = {
        'name': 'Sefrian',
        'age' : '25'
    }
    return render(request, "hello_world.html", context)
def page1(request):
    return render(request, "page1.html")
def page2(request):
    return render(request, "page2.html")