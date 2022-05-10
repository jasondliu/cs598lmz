import mmap
from contextlib import closing
import os
from utils import *
from time import time
import datetime
import sys
import numpy as np
import json
from collections import OrderedDict
import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('--dataset', type=str, default='cora')
parser.add_argument('--batch_size', type=int, default=1)
parser.add_argument('--num_layers', type=int, default=1)
parser.add_argument('--hidden', type=int, default=8)
parser.add_argument('--dropout', type=float, default=0.5)
parser.add_argument('--fastmode', type=bool, default=False)
parser.add_argument('--epochs', type=int, default=200)
parser.add_argument('--lr', type=float, default=0.01)
parser.add_argument('--weight_decay', type=float, default=5e-4)
parser.add_argument('--
