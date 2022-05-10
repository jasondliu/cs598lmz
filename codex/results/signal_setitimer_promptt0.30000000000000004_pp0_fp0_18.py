import signal
# Test signal.setitimer() and signal.getitimer()

# The following test is a bit tricky: we want to test that the timer
# expires after the given delay, but we don't want to sleep() for the
# whole duration of the delay: this would make the test too slow.
# The trick is to use a child process that sleeps for a short time,
# and to use alarm() to limit the time we wait for the child process.
# If the timer expires while the child process is still alive, the
# SIGALRM signal will kill the child process, and the wait() call
# will return immediately.

def handler(signum, frame):
    print("handler")
    raise SystemExit

signal.signal(signal.SIGALRM, handler)

pid = os.fork()
if pid == 0:
    # child process: sleep for a short time
    time.sleep(0.5)
    os._exit(0)

# parent process: set the timer, and wait for the child
signal.setitimer(signal.ITIMER_REAL, 0.2, 0)
pid
