import types
types.FunctionType = types.LambdaType

import os
import sys
import re
import math
import time
import random
import threading
import subprocess
import multiprocessing
import traceback

import numpy as np
import scipy.stats

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

import ROOT
ROOT.gROOT.SetBatch()

import pyroot_logon

import cPickle as pickle

import logging

import argparse

import common_utils as cu
import analysis_utils as au

# ------------------------------------------------------------------------------
#
# main
#
# ------------------------------------------------------------------------------

def main():

    # parse the command line arguments, throw errors if missing any
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-i', '--input',
                        type=str, dest='input',
                        required=True,
                        help='input file')
    args = parser.parse_args()

    # set up logging
    logging.basic
