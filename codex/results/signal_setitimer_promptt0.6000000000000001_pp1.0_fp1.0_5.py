import signal
# Test signal.setitimer (linux timer)
# def signal_handler(signum, frame):
#     print 'signal_handler'
#
# signal.signal(signal.SIGALRM, signal_handler)
# signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
#
# while True:
#     print 'test'
#     time.sleep(0.2)

# Test signal.setitimer (linux timer)
def signal_handler(signum, frame):
    print 'signal_handler'
    signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

signal.signal(signal.SIGALRM, signal_handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

while True:
    print 'test'
    time.sleep(0.2)
