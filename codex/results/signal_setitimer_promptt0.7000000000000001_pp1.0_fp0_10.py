import signal
# Test signal.setitimer/signal.getitimer

import os
import sys

# work around a bug in Python 2.7.6
# http://stackoverflow.com/questions/23463913/unable-to-change-itimer-value
# Fixed in 2.7.7

if sys.platform == 'darwin' and sys.version_info[:3] >= (2, 7, 6):
    if os.environ.get('MACOSX_DEPLOYMENT_TARGET', '') == '':
        import platform
        os.environ['MACOSX_DEPLOYMENT_TARGET'] = platform.mac_ver()[0]

def alarm_handler(signum, frame):
    raise TestFailed("handler called")

def setitimer_lower(when, interval):
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    signal.setitimer(signal.ITIMER_REAL, when, interval)
    signal.setitimer(signal.ITIMER_REAL, 0, 0)
