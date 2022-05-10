import mmap
import argparse
import sys

# TODO: This is to prevent a bug in Mac OS X.  Remove when Apple fixes the OS.
# See: http://bugs.python.org/issue10394
# FIXME: This is a hack!
try:
    import multiprocessing
except ImportError:
    pass

