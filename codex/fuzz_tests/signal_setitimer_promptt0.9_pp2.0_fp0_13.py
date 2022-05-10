import signal
# Test signal.setitimer(): start a timer and be interrupted in a range of time

SLEEP_TOTAL = 10
SLEEP_JITTER = 3
SLEEP_TIME = SLEEP_TOTAL * (1 - random.uniform(0.0, 1.0) * 2 * SLEEP_JITTER / 100)

class SleepInterrupt(Exception):
    pass

def handler(signum, frame):
    raise SleepInterrupt("interrupted")

signal.signal(signal.SIGALRM, handler)

# start the timer
signal.setitimer(signal.ITIMER_REAL, SLEEP_TIME)

# sleep
try:
    time.sleep(SLEEP_TOTAL)
except SleepInterrupt as e:
    print("main:", e)

# timer should be disabled automatically
if signal.getitimer(signal.ITIMER_REAL) == (0.0, 0.0):
    print("main: timer disabled")
