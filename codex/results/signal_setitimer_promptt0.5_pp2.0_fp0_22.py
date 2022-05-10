import signal
# Test signal.setitimer()
#
# We want to test that setitimer() works, but it can't be tested
# reliably from a single process.  So this test starts a child process
# that runs setitimer() and sends us a signal when it's done.  We
# catch the signal and exit with success or failure.

def alarm_handler(signum, frame):
    print("FAIL: timer expired")
    sys.exit(1)

def usr1_handler(signum, frame):
    print("PASS: timer didn't expire")
    sys.exit(0)

signal.signal(signal.SIGALRM, alarm_handler)
signal.signal(signal.SIGUSR1, usr1_handler)

child_pid = os.fork()
if child_pid == 0:
    # Child process
    signal.signal(signal.SIGUSR1, signal.SIG_IGN)

    # Give the parent process a chance to set its signal handlers
    time.sleep(1)

    # Set a 1-second timer
    signal.
