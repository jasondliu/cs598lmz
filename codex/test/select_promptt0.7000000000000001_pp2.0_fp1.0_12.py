import select
# Test select.select behavior on blocking sockets.
import select as _select
_select.select = _select.select_ignore_interrupts
import socket
import sys
import threading
import time
import unittest
import warnings
# Skip test if _multiprocessing wasn't built (e.g. Linux w/ --without-threads).
_multiprocessing = sys.modules.get('_multiprocessing')
mp = sys.modules.get('multiprocessing')
gr = sys.modules.get('multiprocessing.reduction')


def handle_exit(testcase, *args):
    testcase.assertEqual(args, ())
    raise KeyboardInterrupt


def subprocess_main(testcase, conn):
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    testcase.assertEqual(signal.getsignal(signal.SIGINT), signal.SIG_IGN)
    conn.send(os.getpid())
    conn.close()

