import signal
# Test signal.setitimer()
print('\n*** Test signal.setitimer() ***')
def handler(signum, frame):
    print('Signal handler called with signal', signum)
    raise OSError('I am raising')

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.2)
try:
    print('About to sleep')
    time.sleep(1)
except OSError:
    print('Caught OSError')
    
# Test signal.signal()
print('\n*** Test signal.signal() ***')
def handler(signum, frame):
    print('Signal handler called with signal', signum)
    raise OSError('I am raising')

signal.signal(signal.SIGINT, handler)
print('About to sleep')
time.sleep(1)

# Test signal.getsignal()
print('\n*** Test signal.getsignal() ***')
