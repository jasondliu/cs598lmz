import gc, weakref
from multiprocessing import Process, Queue
import time
import numpy as np
from numpy.lib.stride_tricks import as_strided
