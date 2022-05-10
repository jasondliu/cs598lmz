import _struct
import hashlib
import argparse
import itertools
import json
import sys
import string
import logging
import multiprocessing

__version__ = "0.2.0"

_logger = logging.getLogger("ehtim.const")

# Byte codes
NULL = b'\0'
BLOCK_START = b'\0'
BLOCK_END = b'\xff'
BINARY_BLOCK_START = b'B'
ASCII_BLOCK_START = b'A'
BLOCK_END_DATA = b'\1'
BLOCK_END_DATA_END = b'\2'
BLOCK_END_DATA_END_END = b'\3'
BLOCK_END_DATA_END_END_END = b'\4'

# All block byte code possibilities
BLOCK_MARKERS = [BINARY_BLOCK_START, ASCII_BLOCK_START] +\
                [bytes(j) for j in itertools.combinations_with_replacement(
                    [BLOCK
