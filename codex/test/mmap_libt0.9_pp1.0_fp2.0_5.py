import mmap
from os import path
from os import makedirs
from os.path import join
from os import listdir
from operator import itemgetter
from functools import partial
from pdb import set_trace
from cogent.util.misc import parse_command_line_parameters
from numpy import array, min, max, where, nan_to_num, isinf
from cogent.util.table import Table, DataRow
from os.path import split, basename, splitext, dirname, exists


script_info = {}
script_info['brief_description'] = """Convert kallisto output for multiple samples to gpct format"""
script_info['script_description'] = """The script produces a single count table from the output from multiple samples of kallisto.  It handles possible abundancts of the isoforms that may have been generated from expression in a single sample."""
script_info['script_usage'] = []
