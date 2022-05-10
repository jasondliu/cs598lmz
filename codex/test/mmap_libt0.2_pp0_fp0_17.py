import mmap
import os
import re
import sys
import time
import traceback

from collections import defaultdict
from datetime import datetime
from functools import partial
from itertools import chain
from multiprocessing import Pool
from multiprocessing import cpu_count
from multiprocessing import current_process
from multiprocessing import freeze_support
from multiprocessing import Manager
from multiprocessing import Process
from multiprocessing import Queue
from multiprocessing import Value
from multiprocessing import Lock
from multiprocessing import Event
from multiprocessing import Condition
from multiprocessing import Barrier
from multiprocessing import Semaphore
from multiprocessing import BoundedSemaphore
from multiprocessing import Lock
from multiprocessing import RLock
from multiprocessing import Condition
from multiprocessing import Event
from multiprocessing import Semaphore
from multiprocessing import BoundedSemaphore
from multiprocessing import Queue
from multiprocessing import SimpleQueue
from multiprocessing import JoinableQueue
