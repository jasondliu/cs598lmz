import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\n")).start()

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import gym
import pdb

from probabilistic_rl.mdp.stochastic_shortest_path import SPProblem, SPTree
from probabilistic_rl.utils.data_structures import Counter

class Policy:

  def __init__(self, mdp, epsilon=0.01):
    self.mdp = mdp
    self.epsilon = epsilon

    self.V = None
    self.Q = None
    self.policy = None

  def get_action(self, state):
    if state not in self.policy:
      return None

    action = self.policy[state]
    if self.epsilon > 0 and np.random.uniform() < self.epsilon:
      action = self.mdp.sample_action()

    return action

  def get_value(self, state):
    if self.V is None:
      raise
