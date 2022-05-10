import lzma
lzma.filter_decode

"""
import numpy as np
import tensorflow as tf
import subprocess
import os
import time
import logging
import sys


import argparse

parser = argparse.ArgumentParser(description='Train a neural network for audio tagging')
parser.add_argument('--logdir',type=str,default='logdir',help='directory to save logs')
parser.add_argument('--modeldir',type=str,default='models',help='directory to save models')
parser.add_argument('--datadir',type=str,default='data',help='directory to read dataset')
parser.add_argument('--dataset',type=str,default='urban',help='dataset to use')
parser.add_argument('--batch_size',type=int,default=32,help='batch size')
parser.add_argument('--epochs',type=int,default=100,help='number of epochs to train')
parser.add_argument('--learning_rate',type=float,default=1e-3,help='learning rate of
