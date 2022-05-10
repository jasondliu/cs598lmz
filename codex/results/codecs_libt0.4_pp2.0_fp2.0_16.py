import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

def get_data(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def get_article_list(data):
    article_list = []
    for i in data:
        article_list.append(i['article'])
    return article_list

def get_labels(data):
    labels = []
    for i in data:
        labels.append(i['label'])
    return labels

def get_word_list(data):
    word_list = []
    for i in data:
        word_list.append(i['word'])
    return word_list

def get_word_list_2(data):
    word_list = []
    for i in data:
        word_list.append(i['word_2'])
    return word_list

def get_word_list_3(data):
    word_list =
