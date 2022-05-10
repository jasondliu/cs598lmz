import signal
# Test signal.setitimer, case SIGALRM and SIGVTALRM.
import os
import sys
import errno
import time

# Subprocesses exit with this exit code on a timeout.
EXIT_TIMEOUT = 124

# The number of seconds we are willing to wait for a subprocess to finish
# before allowing the test to terminate.  If a subprocess hangs, we still
# allow the test suite to terminate.
TIMEOUT = 60

def rmtree_errorhandler(func, path, exc_info):
    """On Windows, the files in .svn are read-only, so when rmtree() tries to
    remove them, an exception is thrown.  We catch that here, remove the
    read-only attribute, and hopefully continue without problems."""
    import stat
    if not sys.platform in ['win32']:
        raise
    if not os.path.isdir(path):
        # It's a file or a symlink, and they simply can't have the read-only
        # attribute, so we can safely ignore the error.
        return
    # Check for read-only.
