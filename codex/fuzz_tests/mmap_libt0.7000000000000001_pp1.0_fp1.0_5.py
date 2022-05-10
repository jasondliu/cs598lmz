import mmap
import os
import sys
import csv
import re
import subprocess
import datetime
import time
import collections

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
matplotlib.rcParams['axes.facecolor'] = '#eeeeee'
matplotlib.rcParams['axes.edgecolor'] = '#bbbbbb'
matplotlib.rcParams['axes.spines.left'].set_color('#bbbbbb')
matplotlib.rcParams['axes.spines.right'].set_color('#bbbbbb')
matplotlib.rcParams['axes.spines.top'].set_color('#bbbbbb')
matplotlib.rcParams['axes.spines.bottom'].set_color('#bbbbbb')
matplotlib.rcParams['axes.grid'] = 'True'
matplotlib.rcParams['grid.color'] = '#bbbbbb'
matplotlib.rcParams['grid.linestyle
