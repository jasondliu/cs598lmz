import select
# Test select.select(rlist, wlist, xlist, timeout=None)

# Call:
#    select.select(r, w, x, timeout) -> (r1, w1, x1)
# which waits for one of the objects in r to become ready for reading; one of
# the objects in w to become ready for writing; or one of the objects in x to
# have an error condition occur.
#
# If timeout is specified, the waits until one of the events occurs or up to
# timeout seconds have passed. The return value is a triple of lists; each
# triple element contains the objects which became ready. If the time-out
# expires or an error occurs, the return value is three empty lists.

import sys
import socket
import threading
import time
import selectors

def testSelectCases(rlist, wlist, xlist):
    """
    Note: for an object to appear in any list, the object must be in the proper
    state. See table below for the mapping from file objects to states.

    Object  |   read |   write |  except
    --------+--------+--------
