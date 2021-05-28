from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>Hello, world. You're at the polls index.</h2> <div><input type=checkbox id=vehicle1 name=vehicle1 value=bike><label for=vehicle1> I have a bike</label></div>")