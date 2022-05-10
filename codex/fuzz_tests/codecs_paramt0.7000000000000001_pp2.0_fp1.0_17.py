import codecs
codecs.register_error('replace_with_space', codecs.replace_with.space)

def normalize_text(text):
    return unicodedata.normalize('NFD', text).encode('ascii', 'replace_with_space').decode()

def load_data(path):
    data = []
    for filename in os.listdir(path):
        if filename[0] != '.':
            with open(path + filename, 'r') as f:
                data.append(normalize_text(f.read()))
    return data

def load_labels(path):
    labels = []
    with open(path, 'r') as f:
        raw_labels = f.read().split('\n')[:-1]
        for label in raw_labels:
            labels.append(label[-1])
    return labels

def tokenize_text(text):
    return word_tokenize(text)

def vectorize(texts, vocabulary):
    features = []
    for text in texts:
        feature = []
        for word in
