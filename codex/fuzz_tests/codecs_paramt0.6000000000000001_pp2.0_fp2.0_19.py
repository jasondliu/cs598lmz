import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def open_file(filename):
    return codecs.open(filename, 'r', 'utf-8', 'replace_with_space')

def read_file(filename):
    f = open_file(filename)
    content = f.read()
    f.close()
    return content

def remove_stopwords(text):
    stopwords = set(read_file('stopwords.txt').split())
    words = text.split()
    return ' '.join([w for w in words if w not in stopwords])

def stem_words(text):
    stemmer = PorterStemmer()
    words = text.split()
    return ' '.join([stemmer.stem(w) for w in words])

def main():
    text = read_file('text.txt')
    text = remove_stopwords(text)
    text = stem_words(text)
    print(text)

if __name__ == '__main__':
    main()
