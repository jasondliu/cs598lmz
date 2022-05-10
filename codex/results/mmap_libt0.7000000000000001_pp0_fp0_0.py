import mmap
import random
import argparse
import time

from numpy import *

from obj_graph import *
from obj_list import *
from obj_bitset import *
from obj_pool import *

from utils import *


def get_arguments():
    parser = argparse.ArgumentParser(
        description = 'Graph compression tools')
    parser.add_argument('-g', '--graph',
        default = 'data/graph-fb-friends.txt',
        help = 'Input edge list graph')
    parser.add_argument('-n', '--nodes',
        default = 'data/nodes.txt',
        help = 'Input node file')
    parser.add_argument('-o', '--output',
        default = 'out',
        help = 'Output files prefix')
    parser.add_argument('-p', '--pool',
        default = 'pool',
        help = 'Object pool files prefix')
    parser.add_argument('-s', '--samples',
        type = int,
        default = 1000,
        help = '
