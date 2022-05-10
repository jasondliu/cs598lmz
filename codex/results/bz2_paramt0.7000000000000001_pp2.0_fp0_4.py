from bz2 import BZ2Decompressor
BZ2Decompressor

import sys
import os
import glob
from datetime import datetime
from datetime import timedelta
import math
import xml.etree.ElementTree as ET
from multiprocessing import Pool

from collections import defaultdict
import argparse

import numpy as np
import pandas as pd
import holoviews as hv

from bokeh.sampledata import us_counties, unemployment
from bokeh.plotting import *
from bokeh.models import HoverTool
from bokeh.resources import CDN
from bokeh.embed import components
from bokeh.io import export_png, export_svgs

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler

from scipy.sparse import csr_matrix


# In[2]:


# set up directories
data_dir = "data"
output_dir = "output"
viz_dir = "viz"


