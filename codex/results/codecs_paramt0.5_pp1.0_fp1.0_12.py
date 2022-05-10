import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def read_file(path_to_file):
    with codecs.open(path_to_file, "r", encoding='utf-8', errors='replace_with_space') as f:
        data = f.read()

    data = data.lower()
    data = nltk.word_tokenize(data)
    return data

def build_vocab(data):
    counter = collections.Counter(data)
    count_pairs = sorted(counter.items(), key=lambda x: (-x[1], x[0]))

    words, _ = list(zip(*count_pairs))
    word_to_id = dict(zip(words, range(len(words))))

    return word_to_id

def file_to_word_ids(data, word_to_id):
    return [word_to_id[word] for word in data if word in word_to_id]

def load_data():
    train_path = os.path.join(data_path,
