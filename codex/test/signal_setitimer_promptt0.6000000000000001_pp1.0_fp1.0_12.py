import signal
# Test signal.setitimer()
# Test signal.itimer()
# Test signal.getitimer()

# TODO: Test signal.setitimer()

# Test signal.itimer()
import time

def handler(signum, frame):
    print("Alarm!")

signal.signal(signal.SIGALRM, handler)

signal.itimer(signal.ITIMER_REAL, 1)
time.sleep(2)

signal.itimer(signal.ITIMER_PROF, 1)
time.sleep(2)

signal.itimer(signal.ITIMER_VIRTUAL, 1)
time.sleep(2)

# Test signal.getitimer()
print(signal.getitimer(signal.ITIMER_REAL))
print(signal.getitimer(signal.ITIMER_PROF))
print(signal.getitimer(signal.ITIMER_VIRTUAL))
