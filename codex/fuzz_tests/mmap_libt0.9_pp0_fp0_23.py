import mmap,codecs
from collections import defaultdict
from os import listdir
from os.path import isfile, join
import getopt
import sys
from shutil import copyfile
import subprocess
import argparse
from argparse import RawTextHelpFormatter

def main():
    parser = argparse.ArgumentParser(description="Reduces the word frequency in a file to one or the specified most frequent word.\n"+\
            "Default is one instance of the most frequent word per generator.\n", formatter_class=RawTextHelpFormatter)
    parser.add_argument("input", help="input file")
    parser.add_argument("output", help="output file")
    parser.add_argument("--separator", help="separator character in input file (default is \\t)", default="\\t", type=str)
    parser.add_argument("--most", help="number of the most frequent words to extract (default is one)", type=int, default=1)
    parser.add_argument("--verbose", help="show progress", action="store_true")
    parser.add_
