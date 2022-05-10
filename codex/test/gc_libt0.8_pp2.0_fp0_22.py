import gc, weakref
import threading, functools

# in python3, list.index is O(n), which is horrible for
# list-with-indexes, so we use our own indexer
