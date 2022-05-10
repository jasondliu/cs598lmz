import mmap
import datetime
from time import time
from string import *
import sys


def main():
    if len(sys.argv) == 1:
        sys.exit("Usage : python ufop_test.py [test_file] [input_file]")
    elif len(sys.argv) == 2:
        input_file = sys.argv[1]
    elif len(sys.argv) == 3:
        test_file = sys.argv[1]
        input_file = sys.argv[2]
        check_compiled_function(test_file, input_file)
    else:
        sys.exit("Usage : python ufop_test.py [test_file].c [input]")


def check_compiled_function(test_file, input_file):
    start = time()
