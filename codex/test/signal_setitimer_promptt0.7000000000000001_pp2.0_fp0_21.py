import signal
# Test signal.setitimer()

def alarm_handler(signum, frame):
    print("Alarm!")

signal.signal(signal.SIGALRM, alarm_handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

i = 0
while True:
    print("Loop")
    i += 1
    if i == 10:
        break
# Test signal.setitimer()

def alarm_handler(signum, frame):
    print("Alarm!")

signal.signal(signal.SIGALRM, alarm_handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

i = 0
while True:
    print("Loop")
    i += 1
    if i == 10:
        break
 
# Test signal.setitimer()

def alarm_handler(signum, frame):
    print("Alarm!")

signal.signal(signal.SIGALRM, alarm_handler)
signal
