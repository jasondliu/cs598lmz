import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_data(data_dir):
    data = []
    for file in os.listdir(data_dir):
        if file.endswith(".txt"):
            with codecs.open(os.path.join(data_dir, file), 'r', 'utf-8', 'strict') as f:
                data.append(f.read())
    return data

def preprocess_data(data):
    data = [re.sub(r'[^\w\s]', '', text) for text in data]
    data = [re.sub(r'[0-9]', '', text) for text in data]
    data = [re.sub(r'\s+', ' ', text) for text in data]
    data = [text.lower() for text in data]
    return data

def tokenize_data(data):
    return [text.split(' ') for text in data]

def get_vocab(data):
    vocab = []
    for text in data
