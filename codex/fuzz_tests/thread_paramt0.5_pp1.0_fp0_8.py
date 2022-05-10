import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt

import tensorflow as tf
import tensorflow_probability as tfp
tfd = tfp.distributions

import gym
import gym_toy

import time
import pickle

from collections import deque

class Policy:

    def __init__(self, env, agent_name,
                 learning_rate=1e-4,
                 gamma=0.99,
                 entropy_beta=0.01,
                 max_grad_norm=0.5,
                 num_epochs=3,
                 num_train_steps=200,
                 num_env_steps=int(1e6),
                 num_episodes=None,
                 batch_size=64,
                 num_layers=2,
                 hidden_size=256,
                 vf_coef=0.5,
                 start_steps=10000,
                 max_ep_len=1000
