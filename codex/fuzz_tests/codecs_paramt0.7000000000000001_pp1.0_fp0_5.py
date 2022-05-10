import codecs
codecs.register_error('surrogate_escape', codecs.surrogateescape_error)

def get_available_chars_list(path):
    """
    Get the available characters from the corpus.
    """
    all_chars = []
    with codecs.open(path, 'r', 'utf-8', 'surrogate_escape') as f:
        for line in f:
            line = line.strip()
            all_chars.extend(list(line))
    return all_chars

def build_vocab(all_chars, max_vocab_size):
    """
    Get the available characters from the corpus.
    """
    count = collections.Counter(all_chars)
    count_pairs = count.most_common()
    chars, _ = list(zip(*count_pairs))
    chars = ['<pad>', '<unk>'] + list(chars)
    char_to_id = dict(zip(chars, range(len(chars))))

    return chars, char_to_id

def get_seqs(
