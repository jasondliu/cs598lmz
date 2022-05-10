import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("Handler called")
    signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.5, 0)

while True:
    print("Looping")
    time.sleep(1)

# Test signal.setitimer()
# Test signal.setitimer()
# Test signal.setitimer()
# Test signal.setitimer()
# Test signal.setitimer()
# Test signal.setitimer()
# Test signal.setitimer()
# Test signal.setitimer()
# Test signal.setitimer()
# Test signal.setitimer()
# Test signal.setitimer()
# Test signal.setitimer()
# Test signal.setitimer()
# Test signal.setitimer()
# Test signal.setitimer()
# Test signal.setitimer()
# Test signal.setitimer()
#
