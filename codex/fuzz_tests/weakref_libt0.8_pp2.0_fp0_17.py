import weakref

import numpy as np
import tensorflow as tf
import tensorflow_probability as tfp
import tensorflow_probability.python as tfp

from meta_blocks.blocks_base import BlocksBase

tfd = tfp.distributions
tfb = tfp.bijectors
tfu = tfp.util

ACTIVATION_FNS = {
    # "selu": tf.nn.selu,
    # "elu": tf.nn.elu,
    # "tanh": tf.nn.tanh,
    "relu": tf.nn.relu,
    # "softplus": tf.nn.softplus,
}

# TODO: remove this hack
tf.compat.v1.disable_eager_execution()


class BatchNorm(tf.keras.layers.BatchNormalization):
    """
    Custom batch normalization layer that takes a tensor as "training" argument instead of a boolean
    """

    def __init__(self, training, **kwargs):
        super(
