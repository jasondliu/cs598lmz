import signal
# Test signal.setitimer with SIGALRM.
# The above two lines are

# START OMIT
import os


def f(n):
    print(n)
    pid = os.getpid()
    rc = os.fork()
    if rc == 0:
        os.kill(pid, signal.SIGALRM)
    else:
        signal.alarm(1)
        print(signal.alarm(0))
        os.waitpid(rc, 0)


f(4)
# END OMIT
