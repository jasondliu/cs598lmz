import sys, threading
threading.Thread(target=lambda: os.system('pip install fastai==0.7.0')).start()
threading.Thread(target=lambda: os.system('pip install torchtext==0.2.3')).start()
threading.Thread(target=lambda: os.system('pip install torch==0.4.1')).start()
threading.Thread(target=lambda: os.system('pip install bcolz==1.2.1')).start()

from fastai.conv_learner import *
from fastai.text import *
from fastai.model import *
import torchtext
import zipfile as zf
import shutil

from torch import cuda
from torchtext import vocab, data
from torchtext.datasets import language_modeling
from fastai.rnn_reg import *
from fastai.rnn_train import *
from fastai.nlp import *
from fastai.lm_rnn import *
import dill as pickle
import spacy
PATH=Path('data/kaggle/toxic/')//'models'
