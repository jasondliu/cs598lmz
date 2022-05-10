import mmap_utils as m
import os
import sys
import time

parser = argparse.ArgumentParser()
parser.add_argument('-data', type=str, default='data/',
                    help='location of the dataset')
parser.add_argument('-nepoch', type=int, default=100,
                    help='number of training epochs')
parser.add_argument('-nthread', type=int, default=1,
                    help='number of threads for loading data')
parser.add_argument('-nhid', type=int, default=100,
                    help='number of hidden units')
parser.add_argument('-pooling', type=str, default='max',
                    help='type of pooling: max|avg|logsumexp')
parser.add_argument('-noise', type=str, default='',
                    help='additive noise: uniform|normal')
parser.add_argument('-noise_level', type=float, default=0.0,
                    help='noise level')
parser.add_argument('-norm_mask', type=str, default
