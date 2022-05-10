import gc, weakref
import os
import sys
import signal
import time
import threading
import optparse

# from multiprocessing import cpu_count

# from . import config, Connector, Dispatcher, KQ_EV_ADD, \
#     KQ_EV_ADD, KQ_EV_ENABLE, KQ_EV_CLEAR, KQ_EV_DELETE, \
#     KQ_FILTER_READ, KQ_FILTER_WRITE, KQ_FILTER_VNODE, KQ_FILTER_PROC, \
#     KQ_NOTE_DELETE, KQ_NOTE_WRITE, KQ_NOTE_EXTEND, KQ_NOTE_ATTRIB, \
#     KQ_NOTE_LINK, KQ_NOTE_RENAME, KQ_NOTE_REVOKE, \
#     KQ_NOTE_NONE, KQ_NOTE_FUNNEL, KQ_NOTE_EXIT, KQ_NOTE_FORK, \
#     KQ_NOTE_EXEC, KQ_NOTE_REAP,
