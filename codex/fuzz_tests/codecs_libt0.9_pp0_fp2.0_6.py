import codecs
codecs.register(myUTF8Replace)
import pydub
from pydub.utils import mediainfo
from pydub import AudioSegment
from pydub.playback import play
from gtts import gTTS 

# Markov chain using bigram language model 
from nltk import ngrams
from nltk.translate.bleu_score import sentence_bleu
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import FreqDist
from nltk import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk import pos_tag
from random import randint

from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords

from xlrd import *
from xlwt import *
from xlutils.copy import copy

from tempfile import TemporaryFile
import subprocess
import logging
import argparse
import pickle

