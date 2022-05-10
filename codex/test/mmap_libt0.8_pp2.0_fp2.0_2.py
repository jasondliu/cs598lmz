import mmap
import random
import functools
from multiprocessing import Pool
import time
import json
import numpy as np
import os
import argparse

from vocab import Vocab
from dataset import Dataset
from evaluation import get_evaluation

from model import *
from utility import *
from utility import batch_iter
from utility import make_mask
from eval_utility import get_evaluation

def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--save_path", default="model")
    parser.add_argument("--gpu", default=0, type=int)
    parser.add_argument("--load_embedding", default=1, type=int)
    parser.add_argument("--load_model", default=1, type=int)
    parser.add_argument("--update", default=0, type=int)
