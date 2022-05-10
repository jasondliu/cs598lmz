import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def load_data(path):
    with codecs.open(path, 'r', 'utf-8', 'replace_with_space') as f:
        data = f.readlines()
    return data

def build_vocab(data, min_count=0, max_count=None, vocab_size=None):
    # data: list of sentences (words separated by spaces)
    counter = Counter()
    for line in data:
        words = line.strip().split()
        for w in words:
            counter[w] += 1
    if max_count:
        counter = {w: c for w, c in counter.items() if c <= max_count}
    if min_count:
        counter = {w: c for w, c in counter.items() if c >= min_count}
    if vocab_size:
        counter = counter.most_common(vocab_size)

    words, _ = list(zip(*counter.items()))
    word_to_id = dict
