import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import tensorflow as tf
import numpy as np
import pandas as pd
import pickle
import logging
import argparse
import utils
import time
import os

from scipy.sparse import hstack, vstack
from scipy.sparse import csr_matrix
from scipy.sparse import save_npz
from sklearn.preprocessing import normalize
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from math import sqrt

parser = argparse.ArgumentParser(description='Run Disentangled Network.')
parser.add_argument('--model', type=str, default='mf',
                    help='model name: mf, pure_tf, pure_tf_vd, pure_tf_vd_reg, vae, pure_tf_cd_reg, pure_tf_cd_reg_leaky, pure_tf_vd_leaky, pure_tf_vd_reg_leaky, disen_mf,
