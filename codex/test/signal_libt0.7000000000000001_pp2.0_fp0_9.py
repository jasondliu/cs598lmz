import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def index(request):
    return render(request, 'index.html')
