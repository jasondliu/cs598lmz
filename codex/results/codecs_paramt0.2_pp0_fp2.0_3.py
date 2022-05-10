import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def read_data(filename):
    with codecs.open(filename, encoding='utf-8', errors='replace_with_space') as f:
        data = f.read()
    return data

def extract_words(data):
    return re.findall('[a-z]+', data.lower())

def train(features):
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model

NWORDS = train(extract_words(read_data('big.txt')))

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def edits1(word):
    splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes    = [a + b[1:] for a, b in splits if b]
    transposes = [a + b[1] + b[0] + b[2:] for a,
