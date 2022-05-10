import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def blog_single(request):
    return render(request, 'blog-single.html')

def services(request):
    return render(request, 'services.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def portfolio_single(request):
    return render(request, 'portfolio-single.html')

def portfolio_2(request):
    return render(request, 'portfolio-2.html')

def portfolio_3(request):
    return render(request, 'portfolio-3.html')

def portfolio_4(request):
   
