import mmap
import numpy as np
import pickle
import struct
import tempfile

from magent.mancala.mancala_env import MancalaEnv, FlipBoard
from magent.mancala.rules import BaseRule as Rule
from magent.mancala.state import Snapshot
from magent.move import Move
from magent.search_tree.model import Policy
from magent.utils import Cache
from src.algorithms.td_learning import TDLeafParallel


def get_mancala_config(width=8, height=1,
                       feature_planes=4, surround=4,
                       win_reward=1., draw_reward=0., lose_reward=-1., in_row=4):
    return {
        'width': width,
        'height': height,
        'feature_planes': 12,
        'surround': 4,
        'action_space': 2,
        'players': 2,
        'feature_dim': 40 * surround ** 2 + 3 * feature_planes,
        'win_reward': win_re
