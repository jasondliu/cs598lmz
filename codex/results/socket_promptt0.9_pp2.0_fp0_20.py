import socket
# Test socket.if_indextoname() implementation
import test.support
from test.support import get_attribute
import unittest

# Helper class to run an external command with a timeout.
class Program:
    def __init__(self, cmd, args, timeout):
        self.cmd = cmd
        self.args = args
        self.timeout = timeout
        self.returncode = None
        self.errout = bytes()
        self.stdout = bytes()
        self.stderr = bytes()

    def run(self):
        cmdline = [self.cmd]
        cmdline.extend(self.args)
        self.stderr = subprocess.STDOUT
        # Rather than get ourselves tangled up in signals and threads,
        # simply fork a child process to handle the timeout.
        # If the child succeeds, it will set exitcode to 0 and send us an EOF.
        pid = os.fork()
        if pid == 0:
            # Child.  Time out the program and then kill it.
            time.sleep(self.timeout)
            try:
                subprocess.check_call(
