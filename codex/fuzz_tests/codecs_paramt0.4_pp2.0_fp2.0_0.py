import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def utf8_replace(text):
    return text.decode('utf8', 'replace_with_space')

def load_data(path):
    print('Loading data...')
    data = []
    with open(path, 'r') as f:
        for line in f:
            data.append(line.strip())
    return data

def load_data_from_npy(path):
    print('Loading data...')
    data = np.load(path)
    return data

def load_data_from_text(path):
    print('Loading data...')
    data = []
    with open(path, 'r') as f:
        for line in f:
            data.append(utf8_replace(line.strip()))
    return data

def load_data_from_txt(path):
    print('Loading data...')
    data = []
    with open(path, 'r') as f:
        for line in f:
            data.append(line
