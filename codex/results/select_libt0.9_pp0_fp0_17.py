import selectors
import random
import traceback
import logging
import pickle

import numpy as np

from env_actions import ACTIONS as A
from agents import get_agent
from utils import (
    preprocess_input,
    update_score_history,
    _get_possible_actions,
    get_best_direction,
    get_next_position,
    get_possible_actions_with_dist,
    render_env,
)
from args import ARGS as ARGS


def reconstruct_board(board):
    """
    Reconstruct board as rows received as raw input.
    """
    transformed = np.empty((ARGS.rows, ARGS.cols), dtype=np.int8)
    for i, row in enumerate(board):
        new_row = []
        for j, element in enumerate(row):
            new_row.append(element)
        transformed[i, :] = np.array(new_row)
    return transformed


def run():  # pragma: no cover
    """
    This function is the main entry
