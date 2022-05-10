import codecs
codecs.register_error('strict', codecs.ignore_errors)

def read_file(file_name):
    with codecs.open(file_name, encoding='utf-8', mode='r', errors='strict') as f:
        return f.read()

def get_words(raw_text):
    words = raw_text.split()
    return words

def get_sentences(raw_text):
    sentences = raw_text.split('.')
    return sentences

def get_paragraphs(raw_text):
    paragraphs = raw_text.split('\n')
    return paragraphs

def get_top_words(words, top_n=10):
    word_count = Counter()
    for word in words:
        word_count.update([word])
    return word_count.most_common(top_n)

def get_top_bigrams(words, top_n=10):
    bigram_count = Counter()
    for i in range(len(words) - 1):
        bigram_count.update([(words[i], words[i
