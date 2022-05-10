import gc, weakref
import logging
logger = logging.getLogger('rpdb2')

try:
    import queue
except ImportError:
    import Queue as queue

