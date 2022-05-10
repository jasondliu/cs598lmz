import threading
threading.stack_size(67108864) # 64MB stack

# Create your views here.
def index(request):
    #return render(request, 'index.html')
    return HttpResponse('Hello World!')

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))

def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

def home(request):
    tutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    return render(request, 'home.html', {'tutorialList': tutorialList})

def hello(request):
    return render(request, 'hello.html')

def main(request):
    return render(request, 'main.html')

def search_form(request):
    return render(request, 'search_form.html')

def search
