import codecs
codecs.register_error('strict', codecs.ignore_errors)

def build_vocab_from_data(data, min_count=1):
    """ Build vocabulary from list of list of tokens.
    Args:
        data: list of list of tokens.
        min_count: minimum token count.
    Returns:
        vocab: dictionary of token -> index.
        inverse_vocab: dictionary of index -> token.
    """
    vocab = defaultdict(int)
    for tokens in data:
        for token in tokens:
            vocab[token] += 1
    vocab = {token: idx for (idx, (token, count)) in enumerate(vocab.items())
             if count >= min_count}
    inverse_vocab = {idx: token for (token, idx) in vocab.items()}
    return vocab, inverse_vocab

def build_vocab_from_file(path, min_count=1):
    """ Build vocabulary from a file.
    Args:
        path: path to file.
        min_count: minimum token
