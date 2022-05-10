import ctypes
ctypes.cast(ctypes.cdll.LoadLibrary("./libqagent.so"), ctypes.py_object)

import gym
import gym_minigrid
import numpy as np
import matplotlib.pyplot as plt
from sys import path
path.append("./qagent")
from utils import *
from agent import *
import torch

# Create a gym environment
env = gym.make("MiniGrid-Empty-5x5-v0")
env.reset()

# Parameters
num_episodes = int(10e3)
max_steps_per_episode = 200

state_space = env.observation_space.n
action_space = env.action_space.n

# Create an agent
agent = AgentDQN(state_space, action_space, epsilon=1.0, gamma=0.99, lr=1e-3, max_memory_size=int(5e3))

# Training
q_table = False
rewards_list = []

for episode in range(num_episodes):
    env.reset
