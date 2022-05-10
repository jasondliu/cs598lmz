import codecs
codecs.register_error("strict", codecs.ignore_errors)

re_word = re.compile("[A-Za-z]+")
re_punc = re.compile("[\.,!\?;:\(\)]")

def simple_tokenize(sentence):
    return [re_word.sub("", word) for word in sentence.split()]

def strip_punctuation(sentence):
    return re_punc.sub("", sentence)

class Article:
    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.tokens = simple_tokenize(text)

    def _repr_html_(self):
        return """<h2>%s</h2><p>%s</p>""" % (self.title, self.text)

def get_article(title):
    text = wikipedia.page(title).content
    return Article(title, text)

#####

def get_article_titles(word):
    titles = wikipedia.search(word
