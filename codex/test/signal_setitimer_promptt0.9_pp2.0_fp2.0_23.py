import signal
# Test signal.setitimer/getitimer.
ItimerError = Alarm
# class ItimerError(Exception):
#     pass

_ignore = lambda *args: None

# Singleton for the interval timer.
timer_interval = 0
old_alarm = _ignore

def itimer(which, seconds, interval=0):
    """Set one of the interval timers.

    which may be one of ITIMER_REAL, ITIMER_VIRTUAL or ITIMER_PROF
    corresponding to the timers that are decremented in real time, process
    virtual time, or both.

    seconds and interval are in seconds; zero means a polling timer is
    created so that a signal is sent on every clock tick. interval is
    meaningful only for ITIMER_REAL.

    The returned object is a 0-tuple if the timer can't be set. Otherwise,
    a 1-tuple is returned containing, in order, the number of seconds
    remaining before the first signal is sent and the interval time between
    successive signals.
    """

    global timer_interval, old_alarm

