import codecs
codecs.register_error('replace_with_space', codecs.replace_with(' '))

def read_data(file_path):
    """ Read data into a list of strings """
    with codecs.open(file_path, encoding='utf-8', errors='replace_with_space') as f:
        data = f.read().splitlines()
    return data

def build_vocab(data):
    """ Build vocabulary of words """
    counter = collections.Counter(data)
    count_pairs = sorted(counter.items(), key=lambda x: (-x[1], x[0]))

    words, _ = list(zip(*count_pairs))
    word_to_id = dict(zip(words, range(len(words))))
    return word_to_id

def file_to_word_ids(file_path, word_to_id):
    """ Read data into a list of strings """
    data = read_data(file_path)
    return [word_to_id[word] for word in data if word in word_to_id]

def load_data
