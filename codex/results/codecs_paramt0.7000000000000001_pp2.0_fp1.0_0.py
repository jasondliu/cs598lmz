import codecs
codecs.register_error('strict', codecs.ignore_errors)

def load_dictionary(filename, lang='en'):
    wd = {}
    with codecs.open(filename, 'r', encoding='utf8', errors='strict') as f:
        for line in f:
            word, score = line.strip().split('\t')
            if lang == 'en':
                wd[word.lower()] = float(score)
            else:
                wd[word] = float(score)
    return wd

def load_dictionaries(path, lang='en'):
    dictionary = {}
    for fname in os.listdir(path):
        if fname.endswith('.txt'):
            dictionary.update(load_dictionary(os.path.join(path, fname), lang))
    return dictionary

def word_score(word, wd):
    if word in wd:
        return wd[word]
    else:
        return 0

def sentence_score(sentence, wd):
    words = sentence.strip
