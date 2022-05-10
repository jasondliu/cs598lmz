from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = BZ2Decompressor.decompress_nonblocking

#import bz2
#bz2.BZ2Decompressor.decompress = bz2.BZ2Decompressor.decompress_nonblocking

import os
import sys
import signal
import socket
import errno
import select
import logging
import traceback
import threading
import multiprocessing
import multiprocessing.connection
import multiprocessing.managers
import multiprocessing.pool
import multiprocessing.synchronize

from _multiprocessing import Connection

#from multiprocessing.connection import Connection
#from multiprocessing.managers import BaseProxy, BaseManager, SyncManager
#from multiprocessing.pool import Pool
#from multiprocessing.synchronize import Lock, BoundedSemaphore, Semaphore, Condition, Event, Barrier

from multiprocessing.forking import main, Popen, dump, load, ForkingPickler

#from multiprocessing.forking import main, Popen, dump,
