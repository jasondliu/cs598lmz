import codecs
codecs.open('../../data/simplewiki/simplewiki.txt', encoding='utf-8')

import re

def preprocess(text):
    text = re.sub('\n', ' ', text)
    text = re.sub('<.*?>', '', text)
    text = re.sub('[A-Za-z0-9]', '', text)
    text = re.sub(' +', ' ', text)
    return text.strip()

with codecs.open('../../data/simplewiki/simplewiki.txt', encoding='utf-8') as f:
    text = preprocess(f.read())
    print(text[:100])

from collections import Counter

def build_dataset(words, n_words):
    """Process raw inputs into a dataset."""
    count = [['UNK', -1]]
    count.extend(Counter(words).most_common(n_words - 1))
    dictionary = dict()
    for word, _ in count:
        dictionary[word] = len(dictionary)
    data =
