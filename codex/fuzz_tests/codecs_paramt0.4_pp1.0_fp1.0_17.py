import codecs
codecs.register_error('strict', codecs.ignore_errors)

def load_data(path, max_sent_length, max_doc_length, max_word_length):
    data = []
    with open(path, encoding='utf-8', errors='strict') as f:
        docs = []
        sents = []
        words = []
        labels = []
        for line in f:
            if line == '\n':
                if len(words) > 0:
                    sents.append((words, labels))
                    words = []
                    labels = []
                if len(sents) > 0:
                    docs.append(sents)
                    sents = []
                if len(docs) > 0:
                    data.append(docs)
                    docs = []
            else:
                word, label = line.strip().split()
                if len(word) > max_word_length:
                    word = word[:max_word_length]
                words.append(word)
                labels.append(label)
        if len(words) > 0:
            sents.append
