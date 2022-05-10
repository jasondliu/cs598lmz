import mmap
import ctypes
import ctypes.util
import subprocess
import shlex
import os
import time
import re
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import datetime
from matplotlib.backends.backend_pdf import PdfPages

import getpass
import optparse

def parse_options():
    parser = optparse.OptionParser()
