import mmap
import random
import sys
import os
import shutil

from argparse import ArgumentParser
from lib.utils import *

parser = ArgumentParser(description='Benchmarking the server')

# Benchmark Specific
parser.add_argument('--test-file', dest='test_file', default='test_file', help='test file to perform the IO benchmark')
parser.add_argument('--test-timeout', dest='test_timeout', type=int, default=10, help='timeout in seconds for the benchmark')
parser.add_argument('--test-size', dest='test_size', type=int, default=1048576, help='size of the test file in bytes')
parser.add_argument('--test-iterations', dest='test_iterations', type=int, default=10, help='number of times to repeat the test')
parser.add_argument('--test-block-size', dest='test_block_size', type=int, default=1, help='size of the block used by the test in megabytes')

# Test
parser.add_argument('--test', dest='test
