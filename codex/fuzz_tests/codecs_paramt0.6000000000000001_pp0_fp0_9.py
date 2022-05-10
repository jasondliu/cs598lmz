import codecs
codecs.register_error('replace_with_space', lambda e: (u' ',e.start + 1))

def read_txt(txt_file):
    with codecs.open(txt_file, 'r', 'utf-8', 'replace_with_space') as f:
        text = f.read()
        return text

def get_stopwords(stopwords_file):
    with codecs.open(stopwords_file, 'r', 'utf-8', 'replace_with_space') as f:
        stopwords = f.read().split(' ')
        return stopwords

def write_txt(text, txt_file):
    with codecs.open(txt_file, 'w', 'utf-8') as f:
        f.write(text)

def remove_stopwords(text, stopwords):
    text = text.lower()
    text = re.sub('[^\w\s]','',text)
    tokens = text.split(' ')
    tokens = [t for t in tokens if t not in stopwords]
    return tokens

def stem_
