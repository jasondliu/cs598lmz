import socket
# Test socket.if_indextoname() (GH#1417)
import subprocess
import sys
import errno
try:
    import resource
except ImportError:
    resource = None

from _testcapi import raise_exception

def test_exc_info_hidden():
    """Test that sys.exc_info() raises RuntimeError while the thread is
    hidden.

    Issue #20163.
    """
    def run():
        try:
            raise ValueError("test_exc_info_hidden()")
        except ValueError as exc:
            test_support.gc_collect()
            # A thread must be started in order for its exception
            # information to be tracked. This is checked when the thread
            # starts running.
            threading.current_thread().isAlive()
            return exc
    ret_exc = run()
    try:
        type, value, traceback = sys.exc_info()
    except RuntimeError as err:
        assert err.args[0] == ("thread.exc_info() requires active thread",)
