import threading
threading.stack_size(67108864) # 64MB stack

# Create your views here.
def index(request):
    return render(request, 'cache_app/index.html', {})

def get_data(request):
    data = {}
    for key, value in request.POST.items():
        data[key] = value
    return JsonResponse(data)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_calc(request):
    data = {}
    n = int(request.POST['n'])
    data['result'] = fibonacci(n)
    return JsonResponse(data)
