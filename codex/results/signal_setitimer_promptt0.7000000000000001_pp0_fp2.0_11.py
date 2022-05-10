import signal
# Test signal.setitimer() and signal.alarm()

import time

def setitimer_handler(signum, frame):
    print('setitimer_handler: got sig', signum)

def alarm_handler(signum, frame):
    print('alarm_handler: got sig', signum)

signal.signal(signal.SIGALRM, alarm_handler)
signal.signal(signal.SIGVTALRM, setitimer_handler)

print('set alarm() in 1 s')
signal.alarm(1)
time.sleep(2)

print('set itimer() in 2 s')
signal.setitimer(signal.ITIMER_VIRTUAL, 2, 1)
time.sleep(4)
