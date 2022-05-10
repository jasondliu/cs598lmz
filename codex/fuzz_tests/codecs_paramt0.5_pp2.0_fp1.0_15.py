import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def load_vocab(vocab_path):
    """Loads a vocabulary file into a dictionary."""
    vocab = collections.OrderedDict()
    index = 0
    with codecs.open(vocab_path, 'r', encoding='utf-8') as reader:
        while True:
            token = convert_to_unicode(reader.readline())
            if not token:
                break
            token = token.strip()
            vocab[token] = index
            index += 1
    return vocab


def convert_to_unicode(text):
    """Converts `text` to Unicode (if it's not already), assuming utf-8 input."""
    if six.PY3:
        if isinstance(text, str):
            return text
        elif isinstance(text, bytes):
            return text.decode("utf-8", "replace")
        else:
            raise ValueError("Unsupported string type: %s" % (type(text)))
    elif six
