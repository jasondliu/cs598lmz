import codecs
codecs.register_error('strict', codecs.ignore_errors)

import os
import re
import sys
import csv
import glob
import shutil
import logging
import tempfile
import subprocess
import platform
import multiprocessing
import argparse
import traceback

import numpy as np
import pandas as pd

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import average_precision_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score

from sklearn.preprocessing import label_binarize

from sklearn.utils.fixes import signature

#from sklearn.metrics import classification_report

from sklearn.metrics
