import signal
# Test signal.setitimer() using the alarm signal.

import time

def handler(signum, frame):
    global total_time
    total_time += 1
    print('Alarm', total_time)
    if total_time >= 3:
        print('stopping')
        signal.setitimer(signal.ITIMER_REAL, 0)
        return
    signal.setitimer(signal.ITIMER_REAL, 0.1)


signal.signal(signal.SIGALRM, handler)
total_time = 0
signal.setitimer(signal.ITIMER_REAL, 0.1)
while True:
    time.sleep(1)
