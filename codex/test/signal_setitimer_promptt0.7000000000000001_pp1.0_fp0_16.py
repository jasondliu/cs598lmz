import signal
# Test signal.setitimer for bug #1523
signal.setitimer(signal.ITIMER_REAL, 0)
signal.setitimer(signal.ITIMER_VIRTUAL, 0)
signal.setitimer(signal.ITIMER_PROF, 0)

# Test fix for SF bug 1516192
if hasattr(signal, "set_wakeup_fd"):
    signal.set_wakeup_fd(-1)

# Test fix for SF bug 1624234
if hasattr(signal, "set_wakeup_fd"):
    signal.set_wakeup_fd(1)

# Test fix for SF bug 1764907
import time
if hasattr(time, 'tzset'):
    time.tzset()

# Test fix for SF bug 1834239
if hasattr(os, 'forkpty'):
    os.forkpty()

# Test fix for SF bug 1845852
if hasattr(os, 'openpty'):
    os.openpty()

# Test fix for SF bug 1882064
