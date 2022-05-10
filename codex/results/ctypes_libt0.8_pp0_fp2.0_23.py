import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import numpy as np

from tune_cluster import tune_cluster
from prepare_data import load_data, get_train_test_sets, generate_train_test_sets
from classifier import train_classifier
from eval_cluster import eval_cluster
from settings import *
from utils import *
from cluster_dump import get_best_clustering
from hyperopt import fmin, tpe, hp, Trials, STATUS_OK
from cluster import get_cluster_class
from tune_params import run_tune_params

from random import shuffle


def main():
    # tuner_path = "tune_results.pkl"
    # if os.path.isfile(tuner_path):
    #     with open(tuner_path, 'rb') as f:
    #         trials = pickle.load(f)
    #     best = trials.best_trial
    #     print("best hyperparams:", best['result'])
    # else:
    #     trials = Trials
