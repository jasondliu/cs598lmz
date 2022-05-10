import types
types.FunctionType = types.MethodType

import tensorflow as tf
from tensorflow.contrib.seq2seq import *
from tensorflow.python.ops.rnn_cell_impl import GRUCell, LSTMCell

from . import rnn_cell_util

class BasicDecoderOutput(DecoderOutput):
    r"""Basic `DecoderOutput` class.

    Args:
        rnn_output (Tensor): the final output of the decoder.
        sample_id (Tensor): the final output ids of the decoder.
        alignment_history (Tensor): the alignment history from the attention mechanism.

    """
    def __init__(self, rnn_output, sample_id, alignment_history):
        self.rnn_output = rnn_output
        self.sample_id = sample_id
        self.alignment_history = alignment_history


class BasicDecoder(Decoder):
    r"""Basic `Decoder` class.

    Args:
        cell (RNNCell): an RNNCell that will be used to create a recurrent
