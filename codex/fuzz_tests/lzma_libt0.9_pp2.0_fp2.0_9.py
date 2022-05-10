import lzma
lzma.__path__

!python -m pip install xlrd
!python -m pip install scipy
import xlrd
import scipy.io as sio

!python -m pip install numpy
import numpy as np

!python -m pip install scikit_learn
from sklearn.svm import SVC

!python -m pip install pandas
import pandas as pd

!python -m pip install matplotlib
import matplotlib.pyplot as plt

import sys

plt.rcParams.update({'font.size': 12})

def show_values_on_bars(axs, h_v="v", space=0.4):
    
    def _show_on_single_plot(ax):
        
        if h_v == "v":
            for p in ax.patches:
                _x = p.get_x() + p.get_width() / 2
                _y = p.get_y() + p.get_height()
                value = int(p.get_height())
