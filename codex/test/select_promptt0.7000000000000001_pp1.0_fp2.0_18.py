import select
# Test select.select

# Example from http://docs.python.org/library/select.html

from operator import itemgetter

def wait_for_input(rlist, wlist, xlist, timeout=None):
    if timeout is not None:
        end_time = _time() + timeout
    while True:
        rlist, wlist, xlist = select.select(rlist, wlist, xlist)
        if rlist or wlist or xlist:
            return rlist, wlist, xlist
        if timeout is not None:
            timeout = end_time - _time()
            if timeout < 0:
                return [], [], []

# Test different types of input
# see http://bugs.python.org/issue1825

import os, select

