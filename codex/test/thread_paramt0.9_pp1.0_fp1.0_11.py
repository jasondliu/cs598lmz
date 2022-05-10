import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello world\n')).start()

from concurrent.futures import ProcessPoolExecutor
from functools import partial
from multiprocessing import Value
from os import lock, kill, getpid, setpid
from threading import BoundedSemaphore


from contextlib import ExitStack, contextmanager
from itertools import chain
from time import sleep
import multiprocessing


