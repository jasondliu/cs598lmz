import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,ctypes.c_double)

def func(x):
    return x**2
function = FUNTYPE(func)

# create process pool
from multiprocessing import Pool
from multiprocessing import Lock

# close the process pool
from multiprocessing import current_process

from multiprocessing import Process, Queue
from multiprocessing import Lock
from multiprocessing import Event, Condition
from multiprocessing import Semaphore

from multiprocessing import Value

from multiprocessing import Array

from multiprocessing.sharedctypes import Value
from multiprocessing.sharedctypes import Array

from multiprocessing import Pipe

from multiprocessing import Manager
from multiprocessing import Pool

from multiprocessing import Process, Lock, Queue
from multiprocessing import Event, Condition, Semaphore
from multiprocessing import Value, Array, Pipe, Manager

from multiprocessing import Process, Queue
from multiprocessing import current_process

from multiprocessing import
