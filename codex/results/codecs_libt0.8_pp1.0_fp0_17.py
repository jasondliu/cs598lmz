import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Create your views here.
def index(request):
    return render(request, 'index.html')
def addComment(request):
    comment=Comment(text=request.POST['comment'])
    comment.save()
    context={'comments':Comment.objects.all()}
    return render(request, 'result.html', context)
