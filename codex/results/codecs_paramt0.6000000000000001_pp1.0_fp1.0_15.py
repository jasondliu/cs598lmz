import codecs
codecs.register_error('strict', codecs.ignore_errors)


class Tokenizer:
    def __init__(self, token_list):
        self.token_list = token_list

    def tokenize(self, sent):
        sent = sent.lower()
        for token in self.token_list:
            sent = sent.replace(token, ' '+token+' ')
        return sent.split()


def get_tokenizer(token_list):
    return Tokenizer(token_list)


def get_vocab(token_list, vocab_size):
    vocab_dico = {}
    for token in token_list:
        vocab_dico[token] = len(vocab_dico)
    vocab = list(vocab_dico.keys())
    vocab.sort()
    return vocab_dico, vocab


def load_data(data_dir, vocab_dico, vocab, embeddings_index, max_sent_length, tokenizer):
    docs_train = []
    docs_dev = []
    docs
