import signal
# Test signal.setitimer()
#
# src: https://docs.python.org/3/library/signal.html#signal.setitimer

def on_alarm():
    print("Alarm!")
    signal.setitimer(signal.ITIMER_REAL, 0.1)

signal.signal(signal.SIGALRM, on_alarm)
signal.setitimer(signal.ITIMER_REAL, 0.1)

for i in range(5):
    print(i)
    time.sleep(1)
