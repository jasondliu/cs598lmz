import mmap
import numpy as np
import os
import struct
import sys
import time
import threading

from ctypes import *
from functools import reduce
from multiprocessing import Process, Queue
from multiprocessing.managers import BaseManager
from multiprocessing import Pool

from datetime import datetime, timedelta
from copy import copy

from . import _redis_dict
from . import _redis_array
from . import _redis_counter
from . import _redis_lock
from . import _redis_list
from . import _redis_queue
from . import _redis_set
from . import _redis_sorted_set
from . import _redis_string
from . import _redis_bitmap
from . import _redis_hyperloglog
from . import _redis_stream
from . import _redis_geo
from . import _redis_pubsub
from . import _redis_cluster


class Redis(object):
    def __init__(self, **kwargs):
        self.host =
