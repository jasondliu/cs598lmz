import codecs
codecs.register_error('replace_with_space', codecs.lookup('utf-8'))

def load_vocab(vocab_path):
    """
    Load vocabulary file
    :param vocab_path:
    :return:
    """
    vocab_path = os.path.abspath(vocab_path)
    with codecs.open(vocab_path, 'r', 'utf-8') as f:
        words = f.read().splitlines()
    word_to_id = {words[n]: n for n in range(len(words))}
    id_to_word = {n: words[n] for n in range(len(words))}
    return word_to_id, id_to_word


def load_vec(emb_path, vocab_path, n_dim):
    """
    Load pretrained embedding vectors
    :param emb_path:
    :param vocab_path:
    :param n_dim:
    :return:
    """
    vocab_dict, _ = load_vocab(vocab_path
