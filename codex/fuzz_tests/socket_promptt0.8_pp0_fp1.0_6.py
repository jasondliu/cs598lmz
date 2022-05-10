import socket
# Test socket.if_indextoname
import os
import contextlib
import sys
import select

try:
    import fcntl
except ImportError:
    # Skip this test if we don't have fcntl.
    sys.exit(0)

def check(devname, index):
    """Checks if index is the real device index for devname."""
    assert socket.if_indextoname(index) == devname
    assert index == socket.if_nametoindex(devname)

def get_ifi_list():
    # Get the network interfaces
    ifc_list = []
    ifc_names = socket.if_nameindex()
    for (index, name) in ifc_names:
        ifc_list.append(name)
    return ifc_list

@contextlib.contextmanager
def devnull_context():
    # Context manager to redirect stdout and stderr to os.devnull
    # with some systems
    nullfile = open(os.devnull, "wb")
    old_stdout = sys.stdout
    old_stderr
