import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
np.random.seed(1)
import tensorflow as tf
tf.set_random_seed(1)

#import gym
#env = gym.make('CartPole-v0')
#env.seed(1)     # reproducible, general Policy gradient has high variance
#env = env.unwrapped

# get size of state and action from environment
#state_size = env.observation_space.shape[0]
#action_size = env.action_space.n
#print(state_size)
#print(action_size)

#from keras import backend as K

#class Agent(object):
#    def __init__(self, alpha, gamma=0.99, n_actions=4, layer1_size=16, layer2_size=16, input_dims=8):
#        self.gamma = gamma
#        self.lr = alpha
#        self.G = 0
#       
