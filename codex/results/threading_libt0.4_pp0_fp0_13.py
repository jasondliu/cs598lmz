import threading
threading.stack_size(67108864)

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def result(request):
    return render(request, 'result.html')

def upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = DocumentForm()
    documents = Document.objects.all()
    return render(request, 'upload.html', {'documents': documents, 'form': form})

def process(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
       
