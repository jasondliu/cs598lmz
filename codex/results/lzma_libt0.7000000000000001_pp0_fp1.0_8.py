import lzma
lzma.open('data/nltk_data/tokenizers/punkt/PY3/english.pickle.lzma')
 
#print(nltk.sent_tokenize("Hello world, this is a test"))

# Load data
data = open('data/text/data.txt', 'r').read()

# Tokenize words/sentences
sentences = nltk.sent_tokenize(data)
words = nltk.word_tokenize(data)


# Create word frequency dict
def create_word_frequency(words):
    word_frequency = {}
    for word in words:
        if word not in word_frequency:
            word_frequency[word] = 1
        else:
            word_frequency[word] += 1
    return word_frequency


word_frequency = create_word_frequency(words)

# Create scores
def score(sentences):
    scores = {}
    for sentence in sentences:
        for word in nltk.word_tokenize(sentence.lower()):
            if word in word_frequency:
               
