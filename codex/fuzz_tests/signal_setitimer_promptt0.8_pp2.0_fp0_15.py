import signal
# Test signal.setitimer() whether raise an exception
try:
    signal.setitimer(signal.ITIMER_REAL, 1, 1)
except Exception as e:
    print(e)

# Test signal.setitimer() whether raise an exception
try:
    signal.setitimer(signal.ITIMER_PROF, 1, 1)
except Exception as e:
    print(e)

# Test signal.setitimer() whether raise an exception
try:
    signal.setitimer(signal.ITIMER_VIRTUAL, 1, 1)
except Exception as e:
    print(e)
import signal
# Test signal.getitimer() whether raise an exception
try:
    signal.getitimer(signal.ITIMER_REAL)
except Exception as e:
    print(e)

# Test signal.getitimer() whether raise an exception
try:
    signal.getitimer(signal.ITIMER_PROF)
except Exception as e:
    print(e)

# Test signal.getitimer() whether raise an exception

