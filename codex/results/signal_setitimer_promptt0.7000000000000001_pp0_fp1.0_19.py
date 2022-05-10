import signal
# Test signal.setitimer()
def handler1(signum, frame):
    print('Alarm handler 1 called')

signal.signal(signal.SIGALRM, handler1)
signal.setitimer(signal.ITIMER_REAL, 2)

def handler2(signum, frame):
    print('Alarm handler 2 called')

signal.signal(signal.SIGALRM, handler2)
signal.setitimer(signal.ITIMER_REAL, 2)

while True:
    print('Looping')
