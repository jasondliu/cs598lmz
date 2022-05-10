import weakref

import tensorflow as tf

from models.model import Model
from models.utils import *

class Model(Model):
    def __init__(self, config):
        super().__init__(config)
        self.embedding = tf.get_variable("embedding", [self.config.vocab_size, self.config.embed_size])
        self.learning_rate = tf.Variable(0.0, trainable=False)
        self.global_step = tf.Variable(0, trainable=False)
        self.train_summary = []
        self.valid_summary = []

    def build_graph(self):
        self.add_placeholders()
        self.add_embedding()
        self.add_model()
        self.add_loss()
        self.add_train_op()
        self.add_summary()

    def add_placeholders(self):
        self.word_ids = tf.placeholder(tf.int32, shape=[None, None], name="word_ids")
        self.pos_ids = tf.place
