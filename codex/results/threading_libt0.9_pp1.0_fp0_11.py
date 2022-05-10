import threading
threading.stack_size(2**27)
import sys
import os
import io
import logging
import time
import atexit
import re
import tensorflow as tf
import numpy as np
import datetime
import random


def main():
    FLAGS = flags.FLAGS
    for k, v in FLAGS.__flags.items():
        print(k, "=", v)
    
    if tf.gfile.Exists(FLAGS.summaries_dir):
        tf.gfile.DeleteRecursively(FLAGS.summaries_dir)
    tf.gfile.MakeDirs(FLAGS.summaries_dir)
    word_to_id = read_data(FLAGS.train_data_path, FLAGS.test_data_path)
    train_model(word_to_id, FLAGS.seq_length, FLAGS.num_steps, FLAGS.hidden_size, len(word_to_id), FLAGS.batch_size, False, FLAGS)


if __name__ == '__main
