import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def services(request):
    return render(request, 'services.html')

def pricing(request):
    return render(request, 'pricing.html')

def elements(request):
    return render(request, 'elements.html')

def single_blog(request):
    return render(request, 'single-blog.html')

def single_portfolio(request):
    return render(request, 'single-portfolio.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register
