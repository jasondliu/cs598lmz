import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_data(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
    return data

def get_words(data):
    words = []
    for line in data:
        words.append(line.split()[0])
    return words

def get_tags(data):
    tags = []
    for line in data:
        tags.append(line.split()[1])
    return tags

def get_words_tags(data):
    words_tags = []
    for line in data:
        words_tags.append(line.split())
    return words_tags

def get_tags_words(data):
    tags_words = []
    for line in data:
        tags_words.append(line.split()[::-1])
    return tags_words

def get_tags_tags(data):
    tags_tags = []
    for line in data:
        tags_tags.append(line.split()[1::-1])
