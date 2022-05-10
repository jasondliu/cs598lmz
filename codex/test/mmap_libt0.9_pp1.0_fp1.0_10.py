import mmap
import argparse
import glob

# Globals
KB = 1024
MB = 1024*KB
GB = 1024*MB

DEFAULT_STRING_PRINT_WIDTH = 20

DEFAULT_TOTAL_ITERATIONS = 100

# Output control
DEBUG_FLAG = 10*(1<<0)
RAW_DATA_FLAG = 10*(1<<1)

DEFAULT_OUTPUT_FLAGS = DEBUG_FLAG | RAW_DATA_FLAG

# Algo control
ITERATIONS = 1*(1<<0)
MIN_ARRAY_LENGTH = 1*(1<<1)
MAX_ARRAY_LENGTH = 1*(1<<2)
ARRAY_LENGTH_INCREMENT = 1*(1<<3)
ATTEMPTS_PER_ITERATION = 1*(1<<4)

DEFAULT_ALGO_CONTROL = ITERATIONS

#===========================================================================
#                      General Utility Functions
#===========================================================================

def log_msg(outfile, msg, prefix=""):
    now = datetime.now()
    outfile
