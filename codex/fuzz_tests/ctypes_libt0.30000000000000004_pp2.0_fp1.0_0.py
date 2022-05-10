import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
import matplotlib.path as path
import matplotlib.cm as cm
import matplotlib.colors as colors
import matplotlib.colorbar as colorbar
import matplotlib.gridspec as gridspec
import matplotlib.ticker as ticker
import matplotlib.widgets as widgets
import matplotlib.image as mpimg
import matplotlib.lines as mlines
import matplotlib.transforms as mtransforms
import matplotlib.text as mtext

import scipy.integrate as integrate
import scipy.interpolate as interpolate
import scipy.ndimage as ndimage
import scipy.optimize as optimize

import os
import sys
import re
import time
import datetime
import glob
import pickle
import warnings
import argparse
import subprocess
import shutil
import copy
import random

