import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\n")).start()
from IPython.display import Image, display
display(Image(url='https://raw.githubusercontent.com/fjvarasc/DSPXI/master/figures/logo.png'))

x = np.arange(0, 2 * np.pi, 0.3);
np.arange?
# imports, bokeh and holoviews
# all strings and booleans imported from bokeh.sampledata
import numpy as np
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file
import pandas as pd
from functools import reduce
%matplotlib inline
from ipywidgets import interactive
from IPython.display import display
import ipywidgets as widgets
from ipywidgets import *
from scipy import stats
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot
from statsmodels.graphics.tsaplots import *
from statsmodels.tsa.arima_process
