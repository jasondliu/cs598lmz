import select
# Test select.select() call and poll() in the glib event loop.
# For the test we have three read pipes and one write pipe.
# The first read pipe is writing 100 bytes of data at a time.
# The second read pipe is writing 500 bytes of data at a time.
# The third read pipe is writing 1000 bytes of data at a time.

import signal
import time

import gi

from gi.repository import GLib, GObject

def poll_handler(fd, condition):
    #print 'poll_handler'
    print 'poll_handler', fd, 'cond', condition
    buf = os.read(fd, 8)
    print '    read', buf
    return True

# main program
if __name__ == '__main__':
    GObject.threads_init()

    # create the pipes
    (rd1, wr1) = os.pipe()
    (rd2, wr2) = os.pipe()
    (rd3, wr3) = os.pipe()

    # fill them with data
    for i in range(100):
        os.
