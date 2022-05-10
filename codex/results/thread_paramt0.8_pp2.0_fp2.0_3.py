import sys, threading
threading.Thread(target=lambda: sys.stdout.flush()).start()

import numpy as np
np.random.seed(123)
import matplotlib
matplotlib.use('TKAgg')
#matplotlib.use('GTKAgg')
#matplotlib.use('Qt4Agg')
matplotlib.interactive(False)
matplotlib.rc('font', family='sans-serif')
matplotlib.rc('text', usetex=False)
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import glob
import os
import time
import tkinter as Tk
import subprocess

from mb_autoencoder_keras import MDAE_Keras

# Training programs.
from pca_program import PCA_Program
from kmeans_program import KMeans_Program
from mb_autoencoder_program import MDAE_Program


