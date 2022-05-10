import mmap
import os
import sys
import time
import random
import string
import math
import json
import gzip

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable

# SKIP GRAM
class SkipGram(nn.Module):
    def __init__(self, vocab_size=0, embedding_size=0):
        super(SkipGram, self).__init__()
        self.vocab_size = vocab_size
        self.embedding_size = embedding_size

        self.embeddings = nn.Embedding(self.vocab_size, self.embedding_size)
        self.embeddings.weight.data.uniform_(-1.0, 1.0)

        self.embeddings_context = nn.Embedding(self.vocab_size, self.embedding_size)
        self.embeddings_context.weight.data.uniform_(-1.0, 1
