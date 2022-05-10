import threading
threading.stack_size(2**27)

import sys
sys.path.append("../preprocessing/")
from embedding import text_dictionary
from embedding import embedding

sys.path.append("../models/")
from model import Model

def train(dictionary, embedding, config, checkpoint_dir, epochs = 1, batch_size = 32, train_mode = 'new'):
    # start tensorflow session ????
    with tf.Session() as sess:
        # instantiate model
        model = Model(config, sess, dictionary, embedding, checkpoint_dir, batch_size)
        # load model if exists
        model.load(train_mode)
        # train model
        model.train(epochs)

def main():
    # define checkpoint directory
    checkpoint_dir = "./checkpoints"
    # load dictionary
    dictionary = text_dictionary("../data/word_dict.txt")
    # define embedding
    embedding = embedding("../data/glove.6B.50d.txt", dictionary)
    #
