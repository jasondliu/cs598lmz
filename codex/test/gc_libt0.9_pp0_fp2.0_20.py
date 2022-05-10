import gc, weakref
from threading import Thread, Lock

#For supporting Python 3.4 on Pi 3
try:
    import queue
except ImportError:
    # This is here to support python2.7 on a raspberry pi
    import Queue as queue

