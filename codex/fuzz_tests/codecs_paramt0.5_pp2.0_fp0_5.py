import codecs
codecs.register_error('replace_with_space', lambda e: (u' ', e.start + 1))

def read_file(filename):
    with codecs.open(filename, 'r', 'utf-8', 'replace_with_space') as f:
        text = f.read()
    return text

def read_files(path):
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith('.txt'):
                yield os.path.join(root, filename)

def load_files(path):
    rows = []
    index = []
    for filename in read_files(path):
        rows.append({'text': read_file(filename), 'class': os.path.basename(os.path.dirname(filename))})
        index.append(filename)

    data_frame = DataFrame(rows, index=index)
    return data_frame

def get_stop_words():
    result = set()
    for line in open('stopwords_en.txt', 'r
