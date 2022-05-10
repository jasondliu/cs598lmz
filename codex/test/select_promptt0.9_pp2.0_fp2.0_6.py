import select
# Test select.select with a closed socket.

from test import test_support
from test.test_support import TESTFN, unlink
import os

def test_select():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 80))
    sock.close()
    l = [sock]
    l,l,l = select.select(l,l,l, 0)

def test_select_edge_cases():
    '''These test select.select's edge cases as described in
    http://bugs.python.org/issue1140.
    Basically, select.select should allow any numeric type for its fd lists
    and it should do minimal work in computing its result.
    '''

