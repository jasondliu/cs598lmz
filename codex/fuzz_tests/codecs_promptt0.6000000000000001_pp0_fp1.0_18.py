import codecs
# Test codecs.register_error('strict', )

import locale
locale.setlocale(locale.LC_ALL, '')

import os
import re
import sys

import numpy as np

import matplotlib
import matplotlib.pyplot as plt

from matplotlib.backends.backend_pdf import PdfPages

from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib.ticker import MaxNLocator

import subprocess

from math import log10, floor

def round_sig(x, sig=2):
  if x > 0:
    return round(x, sig-int(floor(log10(x)))-1)
  else:
    return 0

########################################################################

def plot_densities(pdf, plot_title, x_label, y_label, x_data, y_data, plot_fname):
  fig = plt.figure(figsize=(8.5,11))
  ax = fig.add_subplot(111)
  ax.set_xlabel(x
