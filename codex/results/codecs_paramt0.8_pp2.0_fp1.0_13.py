import codecs
codecs.register_error('skip', lambda x: (u'?', x.start + 1))

if __name__ == '__main__':

    # Load the data
    def all_pairs():
        for f in glob.glob('data/*.txt'):
            for line in open(f):
                yield line.strip().decode('utf-8', 'skip')
    data = list(all_pairs())

    # Reduce the data
    vocab = {}
    for line in data:
        for word in line[:-1]:
            if word in vocab:
                vocab[word] += 1
            else:
                vocab[word] = 1
    data = [[word.encode('utf-8') for word in line if vocab[word] > 1]
            for line in data if len(line) > 1]

    # Convert strings to integers
    vocab = sorted(vocab)
    vocab = {word: i for (i, word) in enumerate(vocab)}
    data = [[vocab[word] for word in line] for line in data]

   
