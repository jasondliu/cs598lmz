import codecs
codecs.register_error('replace_with_space', lambda e: (u' ', e.start + 1))

# def find_in_array(array, element):
#     for i, item in enumerate(array):
#         if item == element:
#             return i
#     return -1

def find_in_array(array, element):
    try:
        return array.index(element)
    except:
        return -1

def tokenize(text):
    return [tok.strip() for tok in re.split(r'\s+', text) if tok.strip()]

def load_data(filename, max_sent_len=None, max_doc_len=None, vocab=None):
    data = []
    labels = []
    with codecs.open(filename, 'r', 'utf-8', 'replace_with_space') as f:
        for line in f:
            tokens = tokenize(line)
            if len(tokens) > 0:
                if tokens[0] == '__label__1':
                    labels.append
