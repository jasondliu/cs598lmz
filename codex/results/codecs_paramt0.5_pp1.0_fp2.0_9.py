import codecs
codecs.register_error('ignore', lambda x, y: ' ')

def tokenize(text):
    text = text.lower()
    text = text.replace('<br />', ' ')
    text = re.sub('[^a-zA-Z ]', ' ', text)
    text = text.split()
    return text

def get_vocab(texts):
    vocab = set()
    for text in texts:
        vocab |= set(text)
    return vocab

def get_word_to_ix(vocab):
    word_to_ix = {}
    for i, word in enumerate(vocab):
        word_to_ix[word] = i
    return word_to_ix

def get_ix_to_word(vocab):
    ix_to_word = {}
    for i, word in enumerate(vocab):
        ix_to_word[i] = word
    return ix_to_word

def get_embeddings(word_to_ix, embedding_dim, embeddings_path
