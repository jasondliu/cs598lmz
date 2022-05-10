import signal
# Test signal.setitimer()

# This test is a bit tricky.  It tests the setitimer() function, but the
# test itself is run in a child process.  The child process sets up an
# alarm handler, then sets an alarm using setitimer() and then waits
# for a signal.  The parent process then sends the signal.  The child
# process then verifies that the alarm handler was called.

def alarm_handler(signum, frame):
    print "alarm_handler called"
    sys.exit(0)

def main():
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
    print "waiting for signal"
    os.kill(os.getpid(), signal.SIGALRM)
    print "did not get signal"
    sys.exit(1)

pid = os.fork()
if pid == 0:
    # child process
    main()
else:
    # parent process
    os.waitpid(pid, 0)
