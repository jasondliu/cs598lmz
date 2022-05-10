import mmap
import pickle

import numpy as np

import torch
import torch.nn as nn
import torch.nn.functional as F

from transformers import BertTokenizer, BertModel

BATCH_SIZE = args.batch_size
DEVICE = args.device

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
bert = BertModel.from_pretrained('bert-base-uncased')
bert.eval()
bert.to(DEVICE)

num_headers = len(HEADERS)

DATA_PATH = os.path.abspath('../data')

print('reading wiki data from {0}'.format(DATA_PATH))
with open(os.path.join(DATA_PATH, 'train.pkl'), 'rb') as train_f:
    train_data = pickle.load(train_f)
