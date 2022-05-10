import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_data(filename):
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        data = f.read()
    return data

def get_words(data):
    return re.findall(r'\w+', data)

def get_words_set(data):
    return set(get_words(data))

def get_words_dict(data):
    return dict.fromkeys(get_words(data), None)

def get_words_dict_count(data):
    words = get_words(data)
    words_dict = {}
    for word in words:
        words_dict[word] = words_dict.get(word, 0) + 1
    return words_dict

def get_words_dict_count_sorted(data):
    words_dict = get_words_dict_count(data)
    return sorted(words_dict.items(), key=lambda x: x[1], reverse=True)

def get_
