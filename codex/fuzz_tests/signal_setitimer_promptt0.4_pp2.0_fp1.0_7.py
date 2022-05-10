import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("signal")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

while True:
    print("loop")
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
# Test signal.setitimer()
# Test signal.setitimer()
# Test
