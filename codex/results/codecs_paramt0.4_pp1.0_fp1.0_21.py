import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_data(file_name):
    with codecs.open(file_name, 'r', 'utf-8', 'strict') as f:
        data = f.read()
    return data

def get_sentences(data):
    sentences = data.split('\n')
    return sentences

def get_words(sentence):
    words = sentence.split(' ')
    return words

def remove_punctuation(words):
    punctuation = ['.', ',', '!', '?', ':', ';', '"', '\'']
    for word in words:
        if word in punctuation:
            words.remove(word)
    return words

def get_word_count(words):
    word_count = {}
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    return word_count

def get_top_words(word_count, n
