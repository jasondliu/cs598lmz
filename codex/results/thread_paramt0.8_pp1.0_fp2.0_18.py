import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b]2;%s\x07' % sys.argv[1])).start()
import gym
import gym_super_mario_bros
import tensorflow as tf
import numpy as np
import random
import datetime
from src.SuperMarioBrosImport import SuperMarioBrosImport

smb = SuperMarioBrosImport()

load_model=True

class GameWatcher:
    """
    GameWatcher class is responsible for playing the game and collecting the rewards.
    """
    def __init__(self,name):
        """
        Initialize the game.
        :param name: name of the game
        """
        self.name = name
        self.env = gym.make(self.name)
        self.env.reset()
        self.env.render()

    def render(self):
        """
        Render the game.
        """
        self.env.render()

    def get_state(self):
        """
        Get the current state of the game.
        :return: current state
