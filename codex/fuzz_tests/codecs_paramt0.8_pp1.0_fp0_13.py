import codecs
codecs.register_error('replace_with_unknown',
                      lambda error: (u'<UNK>', error.end))
import re
import json

SOS_TOKEN = 0
EOS_TOKEN = 1
UNK_TOKEN = 2
PAD_TOKEN = 3


class Lang:
    def __init__(self, name):
        self.name = name
        self.word2index = {}
        self.word2count = {}
        self.index2word = {0: "SOS", 1: "EOS", 2: "UNK", 3: "PAD"}
        self.n_words = 4  # Count SOS and EOS and UNK and PAD

    def addSentence(self, sentence):
        for word in sentence.split(' '):
            self.addWord(word)

    def addWord(self, word):
        if word not in self.word2index:
            self.word2index[word] = self.n_words
            self.word2count[word] = 1
            self.index2word[self.n_words] = word
