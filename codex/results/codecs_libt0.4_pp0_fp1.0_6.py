import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Create your views here.
def index(request):
    return render(request, 'index.html')

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def handle_uploaded_file(f):
    with open('upload/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def get_data(request):
    file_path = 'upload/'+request.GET['file_name']
    file_name = request.GET['file_name']
    file_type =
