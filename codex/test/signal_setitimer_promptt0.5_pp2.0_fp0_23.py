import signal
# Test signal.setitimer to implement a simple timeout mechanism.
# The test is based on the example from the Python documentation:
# https://docs.python.org/3.4/library/signal.html

def handler(signum, frame):
    print("Forever is over!")
    raise Exception("end of time")

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL,0.1,0.1)

# This will run for 0.1 seconds before raising an exception.
while True:
    pass
