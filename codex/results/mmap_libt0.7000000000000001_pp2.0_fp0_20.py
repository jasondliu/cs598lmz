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
    parser.add_option("-o", "--output", dest="output", default="", \
                      help="The output file where the data will be written", \
                      metavar="FILE")
    parser.add_option("-k", "--kernel", dest="kernel", default=None, \
                      help="The kernel to run the experiment with")
    parser.add_option("-f", "--fault-rate", dest="faultRate", default=None, \
                      help="The fault rate of the system")
    parser.add_option("-r", "--reboot-rate", dest="rebootRate", default=
