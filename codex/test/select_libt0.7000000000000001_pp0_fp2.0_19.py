import select
import subprocess
import errno
import os

# Python 2.6 compatibility
if not hasattr(select, 'poll'):
    import poll as select

# Python 3 compatibility
if hasattr(select, 'poll'):
    poll = select.poll
    POLLIN = select.POLLIN
    POLLHUP = select.POLLHUP
else:
    poll = select.select
    POLLIN = 1
    POLLHUP = 8

class Process(object):
    """Process wrapper for working with subprocess.Popen instances

    This class is used for working with subprocess.Popen instances. It
    reads the input and output of the subprocess and sends the data
    to the given callbacks. The callbacks are executed in the context
    of the Poller instance.

    :param Popen proc: Popen instance to wrap
    """

    def __init__(self, proc):
        self.proc = proc
        self.out = b''
        self.err = b''
        self.on_out = None
        self.on_err = None
