import signal
# Test signal.setitimer() which should be a no-op in Python.
# In the past, a fatal error would occur, resulting in a core dump.
signal.setitimer(signal.ITIMER_REAL, 0.0)


# Issue 1062: when the signal module is reloaded, it should still
# set the interpreter's signal handlers to Python's.
import sys
if sys.platform.startswith('java'):
    raise unittest.SkipTest('jython does not support signal module reloading')
import imp
m = imp.reload(signal)
try:
    import _signal
except ImportError:
    pass


# Issue #1703448: make sure that the alarm() return value is a
# signed int, to match the C alarm() return value
alarm_value = signal.alarm(30)
# alarm() return value should be 0 or positive
if alarm_value < 0:
    raise ValueError("alarm value should be >= 0")
signal.alarm(0)


# Issue #1698983: make sure that itimer errors don't cause a crash
