import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

from eight_mile.utils import SHORT_CIRCUIT
from eight_mile.tf.layers import dense_chain, dy_embeddings_initializer, EmbeddingDropout
from eight_mile.tf.layers import scaled_dot_product_attention, SdpMask
from eight_mile.tf.layers import BERT_ENCODER
from eight_mile.tf.layers import mask_aware_softmax, relu_fn, sigmoid
import tensorflow as tf
from tensorflow.contrib import rnn
from tensorflow.python.ops import rnn_cell_impl
from tensorflow.python.ops import array_ops
from tensorflow.python.ops import init_ops
from tensorflow.python.ops import math_ops
from tensorflow.python.ops import nn_ops
from tensorflow.python.ops import rnn_cell_impl
from tensorflow.python.ops import variable_scope as
