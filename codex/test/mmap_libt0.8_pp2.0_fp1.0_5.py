import mmap
import csv
import re
import math
import ast
import json

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import skimage
import scipy

# import rpy2
# import rpy2.robjects as robjects

from Bio import SeqIO
from itertools import groupby
from tqdm import tqdm
from sklearn import decomposition
from rpy2.robjects.packages import importr
from matplotlib.patches import Ellipse
from scipy.interpolate import RegularGridInterpolator
from scipy.optimize import curve_fit
from iterneighbors import iterneighbors, iterneighbors_bis
from scipy.stats import gaussian_kde
from skimage.transform import rescale, resize, downscale_local_mean
from scipy.spatial.distance import euclidean
from scipy.spatial.distance import pdist
