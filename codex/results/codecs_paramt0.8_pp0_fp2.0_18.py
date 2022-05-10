import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def load_vocab(vocab_path):
    """Loads a vocabulary file into a dictionary."""
    vocab = collections.OrderedDict()
    index = 0
    with codecs.open(vocab_path, 'r', 'utf-8', 'replace_with_space') as reader:
        while True:
            token = convert_to_unicode(reader.readline())
            if not token:
                break
            token = token.strip()
            vocab[token] = index
            index += 1
    return vocab

def convert_by_vocab(vocab, items):
    """Converts a sequence of [tokens|ids] using the vocab."""
    output = []
    for item in items:
        output.append(vocab[item])
    return output

def id_to_word(id_list, vocab_path):
    vocab = load_vocab(vocab_path)
    word = []
    index = 0
    for
