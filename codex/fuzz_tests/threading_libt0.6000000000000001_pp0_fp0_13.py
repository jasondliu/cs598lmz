import threading
threading.stack_size(2**27)
import sys

sys.path.append('./lib')

from train import train_and_evaluate

tf.app.flags.DEFINE_string('buckets', '', 'input data path')
tf.app.flags.DEFINE_string('checkpointDir', '', 'output model path')
tf.app.flags.DEFINE_integer('numEpochs', 0, 'number of epochs')
tf.app.flags.DEFINE_integer('hiddenUnits', 0, 'number of hidden units')
tf.app.flags.DEFINE_integer('trainSteps', 10000,
                            'number of training steps')
tf.app.flags.DEFINE_string('job-dir', '', 'Job dir')
tf.app.flags.DEFINE_string('eval-dir', 'eval', 'Eval dir')
tf.app.flags.DEFINE_boolean('test', False, 'If true, run evals')
tf.app.flags.DEFINE_string('mode', 'train', 'mode: train or eval')
tf.app
