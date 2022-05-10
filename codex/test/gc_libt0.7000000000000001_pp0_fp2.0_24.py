import gc, weakref
from threading import Thread
from multiprocessing import Process
from functools import partial
from queue import Empty as EmptyException
from time import time
