import threading
threading.stack_size(32768)

import sys
sys.path.append('../')

from setup_paths import *
from eval_utils import *

class Evaluator:
    def __init__(self, model, data_dir, model_dir, batch_size, max_steps, args, db_filename=None):
        self.model = model
        self.data_dir = data_dir
        self.model_dir = model_dir
        self.batch_size = batch_size
        self.max_steps = max_steps
        self.args = args
        self.db_filename = db_filename

        self.summary_writer = tf.summary.FileWriter(self.model_dir)

        self.eval_metrics = {}


    def evaluate(self, sess):
        global_step = tf.train.global_step(sess, self.model.global_step_tensor)

