import mmap
import math
import sys
import os
import argparse
import subprocess

#------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------
def print_usage(name):
    print("usage: %s <mapfile> <output_dir> <output_base> <start> <end> <step> <num_threads> <num_blocks> <block_size>" % name)

#------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------
def load_map(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return eval(data)

#------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------
def load_block(filename, block_start, block_size):
    with open(filename, 'r') as f:
        data = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        block = data[block_start:block_start+block_size]
    return block

#------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------
def save_block(filename, block):
    with open(filename, 'w') as f
