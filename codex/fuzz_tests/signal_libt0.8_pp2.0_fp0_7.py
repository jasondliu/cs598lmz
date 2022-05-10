import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Script to run the performance tests
# requires gnuplot to be installed
#
# To Execute:
# python run.py
#
import subprocess
import os
import csv
import datetime
import re

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

base_cmd = 'python peformance.py'
func_cmds = [
    'check_sums',
    'string_manipulation',
    'simple_math',
    'loops'
]

lang_cmds = [
    'java',
    'python'
]

data = {
    'check
