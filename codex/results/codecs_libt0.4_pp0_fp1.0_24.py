import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

#%%
def read_data(filename):
    with open(filename, 'r') as f:
        data = [line.strip() for line in f.readlines()]
    return data

#%%
def build_vocab(data):
    word_counts = Counter(data)
    # Mapping from index to word
    vocabulary_inv = [x[0] for x in word_counts.most_common()]
    # Mapping from word to index
    vocabulary = {x: i for i, x in enumerate(vocabulary_inv)}
    return [vocabulary, vocabulary_inv]

#%%
def build_input_data(data, vocabulary):
    return [vocabulary[word] for word in data if word in vocabulary]

#%%
def load_data():
    print('Loading data...')
    x_text = read_data('data/input.txt')
    y_text = read_data('data/output.txt')
