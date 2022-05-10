import codecs
codecs.register_error('surrogate_escape', codecs.backslashreplace)
class UnicodeStreamFilter:
    def __init__(self, target):
        self.target = target
        self.encoding = 'utf-8'
        self.errors = 'surrogateescape'
        self.encode_to = self.target.encode(self.encoding, self.errors)

    def write(self, s):
        if type(s) == str:
            s = s.encode("utf-8")
        self.encode_to.write(s)

    def flush(self):
        self.encode_to.flush()

import sys
sys.stdout = UnicodeStreamFilter(sys.stdout)
TRAIN_DATA_FILE= 'train.txt'
EVAL_DATA_FILE= 'eval.txt'

with open(TRAIN_DATA_FILE, encoding='utf-8') as f:
    lines = f.read().split('\n')
train_sentences = [line.split('\t') for line in lines]

with open(
