import mmap
import os
import time
import sys
import re
import datetime
import csv
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
from matplotlib.dates import DateFormatter

#------------------------------------------------------------------------------
# Main
#------------------------------------------------------------------------------

def main():

    # Initialize variables
    #---------------------

    # Get the current working directory
    cwd = os.getcwd()

    # Get the command line arguments
    args = get_args()

    # Set the input file name
    if args.infile:
        infile = args.infile
    else:
        infile = cwd + '/' + 'data.csv'

    # Set the output file name
    if args.outfile:
        outfile = args.outfile
    else:
        outfile = cwd + '/' + 'data.png'

    # Set the title
    if args.title:
        title
