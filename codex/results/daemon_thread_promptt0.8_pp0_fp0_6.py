import threading
# Test threading daemon.
from test.support import requires, run_with_locale,reap_children,is_jython
import subprocess
import errno
from test import support
try:
    import threading
    threading.stack_size
except AttributeError: # Extension not available
    threading = None

from test.support.script_helper import assert_python_ok

from test.support import _4G, _4G_
requires(threading and _4G >= 0)

def subinterp(args=()):
    args = (sys.executable, "-Wd", "-c", "pass") + args
    try:
        return subprocess.Popen(args)
    except OSError as e:
        if e.errno != errno.EINVAL:
            raise
        # Issue #14225: some platforms (e.g. OS X 10.5) don't support
        # passing a start_new_session argument to Popen, so try again
        # without.
        return subprocess.Popen(args, close_fds=False)

