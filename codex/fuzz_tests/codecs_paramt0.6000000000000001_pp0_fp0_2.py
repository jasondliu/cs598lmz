import codecs
codecs.register_error('ignore', codecs.lookup('utf-8')[5])

from collections import defaultdict
from copy import deepcopy

from numpy import random

from utils import *

class Config:
    def __init__(self, options):
        self.debug = options.debug
        self.model_name = options.model_name
        self.train_file = options.train_file
        self.dev_file = options.dev_file
        self.test_file = options.test_file
        self.dict_file = options.dict_file
        self.word_emb_file = options.word_emb_file
        self.char_emb_file = options.char_emb_file
        self.word_emb_size = options.word_emb_size
        self.char_emb_size = options.char_emb_size
        self.word_dict_size = options.word_dict_size
        self.char_dict_size = options.char_dict_size
        self.word_rnn_size = options.word_rnn_size
       
