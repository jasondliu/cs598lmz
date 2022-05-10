import signal
# Test signal.setitimer and signal.alarm

def alarm(n):
    print('Alarm!')
    signal.alarm(n)

signal.signal(signal.SIGALRM, alarm)
signal.alarm(2)
signal.setitimer(signal.ITIMER_REAL, 1, 1)

for i in range(10):
    print(i)
    time.sleep(1)

signal.setitimer(signal.ITIMER_REAL, 0, 0)
