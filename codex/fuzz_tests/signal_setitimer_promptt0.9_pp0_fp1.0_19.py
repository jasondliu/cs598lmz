import signal
# Test signal.setitimer, Unix only.
# Make sure a signal occurs in at most 1 second.
import os, sys, signal, traceback, time

timeout = 1.0

def handler(signo, frame):
    print "timeout"
    signal.alarm(0)
    sys.exit(2)

def main():
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, timeout)
    print "putting child to sleep"
    child_pid = os.fork()
    if child_pid == 0:
        time.sleep(1000)
    else:
        time.sleep(2)
        time.sleep(2)
        os.waitpid(child_pid, 0)
    print "done sleeping"

main()
