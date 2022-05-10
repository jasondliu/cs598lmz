import signal
# Test signal.setitimer()
def handler_tick():
    print('Tick')
    signal.setitimer(signal.ITIMER_REAL, 1)
def handler_alarm(x, y):
    print('Alarm: x = ', x, 'y = ', y)
    signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler_alarm)
signal.signal(signal.SIGALRM, handler_tick)

signal.setitimer(signal.ITIMER_REAL, 1)

while True:
    pass
