import mmap
import os
import re
import subprocess
import time
import sys

from collections import defaultdict
from contextlib import closing
from itertools import islice, izip
from Queue import Queue
from Queue import Empty as QueueEmpty
from threading import Thread

from . import gb_utils
from . import sqlitedb


def get_command_line_args():
    """
    """
    # default:
    args = {
        'max_clusters': 0,
        'min_clus_size': 1,
        'max_seq_error': 1,
        'minsampling': 1,
        'threads': 1,
        'output_dir': '.',
        'verbose': False,
        'zipped': False,
        'sample_name': None,
        'cluster_out': False,
        'bypass_umi': False,
        'max_umi_dist': 2,
        'umi_method': 'groom',
        'umi_len': 6,
        'jid': os.getpid(),

