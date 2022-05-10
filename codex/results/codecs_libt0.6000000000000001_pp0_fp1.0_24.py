import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Create your views here.

#这里的路径需要自己改成自己的
CSV_FILE_PATH = '/Users/hongyu/Desktop/crawler/crawler/data/data.csv'

def index(request):
    if request.method == 'POST':
        form = CSVForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect(reverse('crawler:index'))
    else:
        form = CSVForm()
    return render(request, 'index.html', {'form': form})

def handle_uploaded_file(f):
    with open(CSV_FILE_PATH, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


