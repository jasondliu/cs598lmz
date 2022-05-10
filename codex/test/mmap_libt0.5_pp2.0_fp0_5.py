import mmap
import re
import sys
import tempfile

from tqdm import tqdm

from . import utils

try:
    import ujson as json
except ImportError:
    import json


def get_metadata(filename):
    if filename.endswith('.gz'):
        f = gzip.open(filename, 'rb')
    else:
        f = open(filename, 'rb')

    f.seek(0)
