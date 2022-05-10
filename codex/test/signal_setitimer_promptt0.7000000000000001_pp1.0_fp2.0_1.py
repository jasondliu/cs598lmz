import signal
# Test signal.setitimer()
import subprocess
import sys
import time

from . import support


def test_itimer_error():
    support.requires('itimer')
    subprocess.call([sys.executable, "-c",
                     "import signal; signal.setitimer(signal.ITIMER_REAL, 0.2)"])
    time.sleep(1)
    p = subprocess.Popen([sys.executable, "-c",
                          """if 1:
                             import signal
                             def handler(signum, frame):
                                 pass
                             signal.signal(signal.SIGALRM, handler)
                             signal.setitimer(signal.ITIMER_REAL, 0.2)
                          """])
    # If a signal is delivered to the child process before it installs
    # the signal handler, the default SIG_DFL action is to terminate
    # the process, so wait() should not hang
    p.wait()
    time.sleep(0.5)


def test_alarm():
    support.requires('itimer')
