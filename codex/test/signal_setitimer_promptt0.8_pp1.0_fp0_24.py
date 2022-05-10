import signal
# Test signal.setitimer with default argument.
import _testcapi
signal.signal(_testcapi.ITIMER_REAL, lambda x, y: None)
signal.setitimer(_testcapi.ITIMER_REAL)
# Test signal.setitimer with bad type of arguments.
try:
    signal.setitimer([])
except TypeError:
    pass
else:
    print('TypeError expected')
try:
    signal.setitimer(_testcapi.ITIMER_REAL, [], 0)
except TypeError:
    pass
else:
    print('TypeError expected')
try:
    signal.setitimer(_testcapi.ITIMER_REAL, 0, [])
except TypeError:
    pass
else:
    print('TypeError expected')
try:
    signal.setitimer(_testcapi.ITIMER_REAL, 0, 0, [])
except TypeError:
    pass
else:
    print('TypeError expected')
