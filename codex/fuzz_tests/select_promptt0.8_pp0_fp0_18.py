import select
# Test select.select and built-in file objects

import socket
import sys
import os
import select
import threading

# Test select.select
print "Testing select.select"

# Check basic functionality
rfd, wfd = os.pipe()
rfd2, wfd2 = os.pipe()

try:
    r, w, x = select.select([rfd, rfd2], [wfd], [])
    if (r != [rfd] or w != [wfd] or x != []
        or not hasattr(r[0], "fileno")
        or not hasattr(w[0], "fileno")):
        raise RuntimeError("Bad return values from select.select", r, w, x)
finally:
    os.close(rfd)
    os.close(wfd)
    os.close(rfd2)
    os.close(wfd2)


# Check exception handling and objects with fileno() methods.
class FileLike:
    def __init__(self):
        self.read_evt = threading.Event()

   
