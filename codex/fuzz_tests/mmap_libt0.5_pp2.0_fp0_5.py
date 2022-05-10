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
    first = f.readline()
    f.seek(-1024, 2)
    last = f.readlines()[-1]

    first = json.loads(first)
    last = json.loads(last)

    return first['created_at'], last['created_at']


def get_tweet_ids(filename):
    ids = set()

    if filename.endswith('.gz'):
        f = gzip.open(filename, 'rb')
    else:
        f = open(filename, 'rb')

    with f:
        for line in f:
            tweet = json.loads(
