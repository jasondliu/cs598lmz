import signal
# Test signal.setitimer() and signal.getitimer().

def handler(signum, frame):
    "Handler for alarm signal."
    global alarm_fired
    alarm_fired = 1

counter = 0

def handler1(signum, frame):
    "Handler for realtime signal."
    global counter
    counter += 1
    print('handler1 called at', time.time())


signal.signal(signal.SIGALRM, handler)

# Set an alarm.
signal.setitimer(signal.ITIMER_REAL, 1, 0.5)

for i in range(3):
    print('Waiting', i + 1)
    time.sleep(1)

assert counter == 2

signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler1)

signal.setitimer(signal.ITIMER_REAL, 0.2, 0.2)

for i in range(3):
    print('Waiting', i + 1)
