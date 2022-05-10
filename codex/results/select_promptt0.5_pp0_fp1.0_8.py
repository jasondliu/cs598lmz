import select
# Test select.select()
import socket
import sys
import time

from . import util

from . import test_support

# Don't let the tests run forever
timeout = test_support.get_attribute(select, "set_timeout")
if timeout is not None:
    timeout(10)

if hasattr(select, 'PIPE_BUF'):
    PIPE_BUF = select.PIPE_BUF
else:
    PIPE_BUF = 512

# Some platforms seem to have problems with select(), so we'll give it
# a bit of help.
def select_ignore_interrupts(*args):
    while True:
        try:
            return select.select(*args)
        except (OSError, select.error) as e:
            if e.args[0] == errno.EINTR:
                continue
            raise

# Helpers for creating connected sockets;
# a simple replacement for test_socket.

def open_socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0):
   
