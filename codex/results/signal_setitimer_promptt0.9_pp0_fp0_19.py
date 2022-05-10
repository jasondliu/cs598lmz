import signal
# Test signal.setitimer()
import sys
if hasattr(signal, 'setitimer'):
    signal.setitimer(signal.ITIMER_REAL, 2.0)
    sleep(1)
    signal.alarm(0)
    if sys.platform != 'win32':
        signal.setitimer(signal.ITIMER_PROF, 2.0)
    signal.signal(signal.SIGALRM, lambda a,f: None)
# test signal.signal()
if hasattr(signal, 'SIGWINCH'):
    from test_signal import check_signal_catch
    check_signal_catch(signal.SIGWINCH)

# test relpath()
from os.path import curdir, pardir
from os.path import join
from os.path import abspath, normpath, normcase
from os.path import relpath

def check_relpath(path, start=curdir):
    "Common functionality to test that relpath returns the expected values"
    if not path:
        raise ValueError("check_
