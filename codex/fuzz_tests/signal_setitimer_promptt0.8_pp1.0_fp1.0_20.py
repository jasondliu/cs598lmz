import signal
# Test signal.setitimer

from test_support import verbose, get_original_stdout
from time import sleep, time

def handler(signum, frame):
    raise RuntimeError, "alarm"

def test():
    if verbose:
        print "Testing setitimer... ",
    signal.signal(signal.SIGALRM, handler)

    alarm_seconds = 1.0
    # Determine whether or not we can set an alarm for less than one second
    while 1:
        now = time()
        sleep(alarm_seconds)
        if time() - now >= alarm_seconds:
            break
        alarm_seconds = alarm_seconds / 2.0

    to_save = signal.setitimer(signal.ITIMER_REAL, alarm_seconds)
    if verbose:
        print to_save,
    sleep(alarm_seconds / 2.0)
    if verbose:
        print signal.setitimer(signal.ITIMER_REAL, 0),
    try:
        signal.setitimer(signal.ITIMER_REAL
