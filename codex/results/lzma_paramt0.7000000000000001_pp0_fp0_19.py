from lzma import LZMADecompressor
LZMADecompressor()

import sys
import logging
import os
import json
import gzip
import bz2
import lzma
from datetime import datetime
from multiprocessing import Process, Queue
import re

from .utils import reader
from .utils import gzreader
from .utils import bz2reader
from .utils import lzreader

logger = logging.getLogger(__name__)


def _worker(in_queue, out_queue, fields_to_extract):
    """The worker function, invoked in a process.

    Args:
        in_queue (Queue): The read queue.
        out_queue (Queue): The write queue.
        fields_to_extract (dict): a dictionary of all fields to extract.
    """
    while True:
        item = in_queue.get()
        if item is None:
            break

        fn = item
        if fn.endswith(".gz"):
            with gzreader(fn) as f:
                for line in f:
                    if line.startswith("#"):
                       
