import codecs
codecs.register_error('ignore_unimportant', IgnoreUnimportant)

class IgnoreUnimportant(Exception):
    '''ignore this token'''

# 增加一个名为ignore_unimportant 的错误类型,
# 每次遇到不重要的词,就抛出此异常, 这时不做任何处理,
# 接着处理下一个词

class MyTokenizer(object):
    def __init__(self, text):
        self.text = text
        self.offset = 0
        self.tokens = []
    def tokenize(self):
        raw_tokens = self._tokenize(self.text)
        self.tokens = [tok for tok in raw_tokens if tok not in self.unimportant]
    def _tokenize(self, text):
        while text:
            m = self.word_
