import socket, errno
import threading, time

import testenv; testenv.configure_for_tests()
import fcntl, termios
from test_support import captured_output, do_thread_tests, TestFailed, is_jython

# Support for tests
def segfault(arg):
    time.sleep(0.1)
    # Do something that will turn a pdb into a mess:
    # first use an abbreviation for the standard output name
    import sys
    savestdout = sys.stdout
    disable_stdout = False
    if not is_jython:
        isnonblock = lambda fd: fcntl.fcntl(fd, fcntl.F_GETFL) & os.O_NONBLOCK
        # Temporarily disable stdout buffering, so that we can get a
        # potentially recursive segfault's output as fast as possible.
        if arg and hasattr(sys.stdout, 'fileno'):
            disable_stdout = not isnonblock(sys.stdout.fileno())
