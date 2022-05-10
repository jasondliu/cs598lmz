import codecs
codecs.register_error('replace_with_unknown', lambda e: (u'[UNK]', e.end))

class Preprocessor(object):
    def __init__(self, max_len=600, vocab_size=50000, oov='<UNK>'):
        self.max_len = max_len
        self.vocab_size = vocab_size
        self.oov = oov
        self.index_from = 3
        self.word_to_id = None
        self.id_to_word = None
        self.word_count = None
        self.word_doc_count = None

    def get_word_count(self, text, count_doc=False):
        """
        :param text: list of list, 一个文档是一个list， 每个list中的每个元素是该词在该文档中出现的次数
        :param count_doc: boolean, default False
        :return:
