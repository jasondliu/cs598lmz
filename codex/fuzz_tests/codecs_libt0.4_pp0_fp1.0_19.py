import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

def get_data(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            data.append(line.strip())
    return data

def get_words(data):
    words = []
    for line in data:
        for word in line.split():
            words.append(word)
    return words

def get_words_from_file(filename):
    data = get_data(filename)
    words = get_words(data)
    return words

def get_words_from_files(filenames):
    words = []
    for filename in filenames:
        words += get_words_from_file(filename)
    return words

def get_words_from_dir(dirname):
    filenames = os.listdir(dirname)
    filenames = [dirname + '/' + filename for filename in filenames]
    return get_
