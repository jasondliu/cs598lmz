import codecs
codecs.register_error('surrogate_escape', codecs.surrogateescape_error)

def get_data(path):
    data = []
    for line in open(path, 'r'):
        line = line.strip().split('\t')
        data.append(line)
    return data


def get_label(path):
    labels = []
    for line in open(path, 'r'):
        line = line.strip()
        labels.append(line)
    return labels


def get_word_dict(data):
    word_dict = {}
    for line in data:
        for word in line:
            word_dict[word] = word_dict.get(word, 0) + 1
    return word_dict


def get_max_len(data):
    max_len = 0
    for line in data:
        if len(line) > max_len:
            max_len = len(line)
    return max_len


def get_word_embedding(word_dict, embedding_path, embedding_dim=300):
   
