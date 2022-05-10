import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    full_text = request.GET['fulltext']
    word_list = full_text.split()
    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            #Increase
            word_dictionary[word]+=1
        else:
            #add to the dictionary
            word_dictionary[word]=1

    return render(request, 'result.html', {'fulltext':full_text, 'total':len(word_list), 'dictionary':word_dictionary.items()})
