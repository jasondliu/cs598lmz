import ctypes
ctypes.windll.user32.SetProcessDPIAware()

# Create your views here.
def home(request):
    return render(request, 'index.html')
