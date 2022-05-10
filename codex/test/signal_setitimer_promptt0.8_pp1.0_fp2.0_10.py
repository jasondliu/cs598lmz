import signal
# Test signal.setitimer() and signal.setitimer()
# and it is used to send signal in python

def signal_handler(num, stack):
    print('Received signal {} in handler'.format(num))

signal.signal(signal.SIGALRM, signal_handler)
signal.setitimer(signal.ITIMER_REAL, 2)
print('Signal handler set to {}'.format(signal_handler))
print('Sleeping for 10 seconds')
time.sleep(10)

signal.setitimer(signal.ITIMER_REAL, 0)
print('Timer disabled')
time.sleep(5)
