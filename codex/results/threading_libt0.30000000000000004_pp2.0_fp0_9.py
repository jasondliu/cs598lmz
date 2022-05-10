import threading
threading.stack_size(67108864) # 64MB stack

# Create your views here.
def index(request):
    return render(request, 'index.html')

def upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {
        'form': form
    })

def start_processing(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {
        'form': form
    })

def process_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
       
