import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
signal.signal(signal.SIGPIPE, signal.SIG_DFL)
####

LEMMA_DICTIONARY_PATH = "/home/rolaharmouche/wikidump/Lemma_Dictionary.tsv"
RULE_SET_PATH = "/home/rolaharmouche/wikidump/Rule_Set_Wiki.tsv"

import os
import sys
import torch
import stopit
from argparse import ArgumentParser
from collections import defaultdict
from sklearn.model_selection import train_test_split
from pytorch_pretrained_bert import BertTokenizer
from pytorch_pretrained_bert import BertForNextSentencePrediction
from pytorch_pretrained_bert import BertConfig
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader

import numpy as np

parser = ArgumentParser()
