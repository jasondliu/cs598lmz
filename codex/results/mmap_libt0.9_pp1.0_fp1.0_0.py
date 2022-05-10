import mmap
import os
import sys
import traceback
from string import *
import datetime
import math
from math import *
import operator
from optparse import OptionParser
import csv
import subprocess
from __builtin__ import str
import bisect


def read_stdin():
    """Reads pages from stdin
    Extracts the first few lines of each page and returns a map of title -> content
    Content is a list of lines"""
    pages = {}
    current_title = None
    current_content = []
    for line in sys.stdin:
        line = line.strip() # ignore trailing spaces
        if current_title is None and line.startswith("<page>"):
            # start of page
            current_title = None
            current_content = []
        elif current_title is not None and line.startswith("</page>"):
            # end of page
            pages[current_title] = current_content
            current_title = None
            current_content = []
        elif current_title is None and line.startswith("<title>"):
