import lzma
lzma.open

import os
import sys
import time
import shutil
import argparse
import subprocess
import multiprocessing
import multiprocessing.pool

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from torch.utils.data.sampler import SubsetRandomSampler
from torch.utils.data.dataloader import default_collate

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

from tqdm import tqdm

from utils import *
from model import *
from dataset import *

def main():
    parser = argparse.ArgumentParser(description='Train a model on the dataset')
    parser.add_argument('--dataset', type=str, default='data/dataset.csv',
                        help='path to
