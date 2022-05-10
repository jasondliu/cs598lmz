import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import argparse
import os
import sys
import codecs
import signal
import gc
import time
import traceback

import nltk
from nltk.internals import find_jars_within_path
from nltk.tag import StanfordNERTagger

from nltk.tokenize import *

from . import *


class StanfordNER:
    def __init__(self, path_to_jar, path_to_models, encoding='utf8'):
        self.path_to_jar = path_to_jar
        self.path_to_models = path_to_models
        self.encoding = encoding
        self.tagger = StanfordNERTagger(
            os.path.join(self.path_to_models, 'ner-model.ser.gz'),
            path_to_jar=path_to_jar,
            encoding=encoding)

    def tag(self, words):
        return self.tagger.tag(words)

