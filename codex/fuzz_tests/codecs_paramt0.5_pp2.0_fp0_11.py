import codecs
codecs.register_error('strict', codecs.ignore_errors)

# logging
import logging
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

import os
import sys
import argparse
import cPickle as pickle

import numpy as np
import theano
import theano.tensor as T
import lasagne

from nn import build_model, iterate_minibatches, gen_embeddings
from utils import Progbar, minibatches

def main(num_epochs=50,
         batch_size=128,
         num_classes=2,
         num_units=128,
         learning_rate=0.001,
         grad_clipping=5,
         embedding_size=128,
         embedding_dropout=0.5,
         embeddings=None,
         embeddings_trainable=False,
         saveto='model.npz',
