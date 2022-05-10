import mmap
import csv
import os
import os.path
import sys
import re
import time
import argparse
from io import StringIO
from collections import defaultdict
from operator import itemgetter

def main():
    parser = argparse.ArgumentParser(description='Analyze a set of runs of a workload')
    parser.add_argument('--dir', '-d', help='directory where the runs are stored', required=True)
    parser.add_argument('--title', '-t', help='title for the plot', required=True)
    parser.add_argument('--output', '-o', help='output file', required=True)
    parser.add_argument('--outliers', '-r', help='outlier runs', default=None)
    parser.add_argument('--filter', '-f', help='filter pattern', default='.*')
    parser.add_argument('--nofilter', '-n', help='do not filter', action='store_true')
    parser.add_argument('--skip', '-s', help='skip columns', default=0
