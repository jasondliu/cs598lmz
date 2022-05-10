import codecs
codecs.register_error('replace_with_space', codecs.lookup_error('replace_with_space'))

def read_data(filename):
    with codecs.open(filename, encoding='utf-8', errors='replace_with_space') as f:
        data = f.read()
    data = data.lower()
    data = re.sub(r'[^a-z\s]', ' ', data)
    data = re.sub(r'\s+', ' ', data)
    return data.strip().split()

def build_vocab(words):
    word_to_id = {}
    id_to_word = {}

    for word in words:
        if word not in word_to_id:
            new_id = len(word_to_id)
            word_to_id[word] = new_id
            id_to_word[new_id] = word

    return word_to_id, id_to_word

def file_to_word_ids(filename, word_to_id):
    data = read_data(filename)
