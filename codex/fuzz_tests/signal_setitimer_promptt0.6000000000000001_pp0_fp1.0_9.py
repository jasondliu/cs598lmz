import signal
# Test signal.setitimer()


def handler(signum, frame):
    print("Signal handler called with signal", signum)


print("Registering")
signal.signal(signal.SIGALRM, handler)

print("Starting the timer")
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

try:
    print("Sleeping")
    time.sleep(2)
except InterruptedError:
    print("Got a signal while sleeping")

print("Turning off the timer")
signal.setitimer(signal.ITIMER_REAL, 0)

print("Done")
