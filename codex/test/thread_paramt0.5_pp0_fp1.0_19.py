import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()
import os, shutil

from src.config import Config
from src.env import Env
from src.agent import Agent
from src.utils import *

from src.model.dqn import DQN
from src.model.ddqn import DDQN
from src.model.cnn import CNN
from src.model.mlp import MLP

from src.data.data_generator import DataGenerator
from src.data.data_process import DataProcess

from src.train.train_rl import TrainRL
from src.train.train_sl import TrainSL

from src.test.test_rl import TestRL
from src.test.test_sl import TestSL


def train(config, data_process, data_generator, env, agent, model):
    train_rl = TrainRL(config, data_process, data_generator, env, agent, model)
    train_rl.run()

