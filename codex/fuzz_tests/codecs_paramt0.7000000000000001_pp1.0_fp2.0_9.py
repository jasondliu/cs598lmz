import codecs
codecs.register_error('replace_with_space', lambda e: (u' ', e.start + 1))

def load_glove(file_name):
    """
    Loads GloVe matrix from file.
    """
    with codecs.open(file_name, 'r', 'utf-8') as f:
        matrix = np.loadtxt(f)
        
    return matrix

# Load GloVe matrix
glove = load_glove(glove_s50_path)

# Map word to GloVe index
word_to_glove_index = {}

for i, word in enumerate(vocab_to_int.keys()):
    word_to_glove_index[word] = i

# Create matrix of GloVe vectors
glove_matrix = np.zeros((len(vocab_to_int), 50), dtype=np.float32)

for word, i in vocab_to_int.items():
    glove_index = word_to_glove_index.get(word, None)
    
    if glove_index
