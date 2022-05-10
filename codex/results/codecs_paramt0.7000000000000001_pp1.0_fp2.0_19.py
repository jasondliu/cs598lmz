import codecs
codecs.register_error('strict', codecs.ignore_errors)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.backends.backend_pdf import PdfPages
import seaborn as sns
import numpy as np
import pandas as pd
import random
import os
import sys
import glob
import pprint
import argparse

from matplotlib.patches import Circle, Rectangle, Arc

from src.fancyplots import *

# plotting parameters
sns.set_context(context='paper',font_scale=1)
sns.set_style(style='white')


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--input',type=str)
    parser.add_argument('-o','--output',type=str)
    parser.add_argument('-l','--label',type=str)
    args = parser.parse_args()

    fig = plt.
