import signal
# Test signal.setitimer()
# This just tests that it works and it formats properly
def handler(signum, frame):
    print( signum, frame)

signal.signal(signal.SIGALRM, handler)

for i in range(5):
    print('setitimer ', signal.setitimer( signal.ITIMER_REAL, i + 0.1, 1))

print(signal.getitimer( signal.ITIMER_REAL))

print(signal.getitimer( signal.ITIMER_REAL))


try:
    for i in range(10):
        time.sleep( 0.01)
except KeyboardInterrupt:
    pass

print(signal.getitimer( signal.ITIMER_REAL))
print(signal.getitimer( signal.ITIMER_VIRTUAL))
print(signal.getitimer( signal.ITIMER_PROF))

print(signal.getitimer( signal.ITIMER_REAL))
print(signal.getitimer( signal.ITIMER_
