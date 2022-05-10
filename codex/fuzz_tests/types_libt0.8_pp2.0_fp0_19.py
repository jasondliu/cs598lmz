import types
types.SimpleNamespace = types.Namespace

import gym

NUM_ACTIONS = 4
TARGET_UPDATE = 100
NUM_STEPS = 2000000
MAX_STEPS_PER_EPISODE = 5000
REPLAY_START_SIZE = 50000
BATCH_SIZE = 32
GAMMA = 0.99

def make_env(env_str, render=False):
    env = gym.make(env_str)
    if render:
        env = Render(env)
    return env

class Render(gym.Wrapper):
    def __init__(self, env):
        super(Render, self).__init__(env)
        self.metadata['video.frames_per_second'] = 1
        self.metadata['video.width'] = 600


class ReplayMemory:
    def __init__(self, capacity):
        self.capacity = capacity
        self.memory = []
        self.position = 0

    def push(self, transition):
        if len(self.memory) < self.capacity:
            self.memory.append(None)
       
