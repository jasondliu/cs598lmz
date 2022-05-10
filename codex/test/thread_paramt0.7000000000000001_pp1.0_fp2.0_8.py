import sys, threading
threading.Thread(target=lambda: sys.stderr.write('\x1b[2J\x1b[H')).start()

from Agent import Agent
from Environment import Environment
from utils import plotLearning
from time import sleep
import numpy as np
from keras.models import load_model
from keras import backend as K
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras.models import load_model
from keras.models import model_from_json
import h5py
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.Session(config=config)
K.set_session(sess)

# if __name__ == '__main__':
#     np.random.seed(1)
#     env = Environment()
#     agent = Agent(gamma=0.99, epsilon=1.0, batch_size=64, n_actions=2, eps_end=0.01, input_dims
