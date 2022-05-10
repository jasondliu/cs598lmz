import codecs
codecs.register_error('strict', codecs.ignore_errors)

from os import path

from nltk.tokenize.punkt import PunktWordTokenizer
from nltk.tokenize.punkt import PunktSentenceTokenizer
from nltk.tokenize.punkt import PunktParameters
from nltk.tokenize.punkt import PunktTrainer

from nltk.tokenize.treebank import TreebankWordTokenizer
from nltk.tokenize.treebank import TreebankWordDetokenizer

from nltk.corpus.reader.plaintext import CategorizedPlaintextCorpusReader

class Tokenizer(object):

    def __init__(self, lang, case_sensitive=False, **kargs):
        self.lang = lang
        self.case_sensitive = case_sensitive
        self.tokenizer = None
        self.detokenizer = None
        self.train(**kargs)

    def train(self, **kargs):
        pass

    def tokenize(self, s):
        pass

    def detokenize(self, l
