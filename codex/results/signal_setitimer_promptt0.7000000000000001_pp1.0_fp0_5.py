import signal
# Test signal.setitimer()
# Run the test code in a subprocess, so we can kill it if it goes too long.
# This is a workaround for an apparent bug in signal.setitimer() on FreeBSD.
# See http://bugs.python.org/issue1696015
# and http://bugs.python.org/issue1696016
pid = None

def handler(signum, frame):
    if pid:
        os.kill(pid, signal.SIGKILL)
    raise RuntimeError("timeout")

signal.signal(signal.SIGALRM, handler)

try:
    signal.setitimer(signal.ITIMER_REAL, 0.02)
    pid = os.fork()
    if pid == 0:
        # child
        signal.setitimer(signal.ITIMER_REAL, 0.1)
        time.sleep(0.3)
        os._exit(0)
    else:
        # parent
        pid, sts = os.waitpid(pid, 0)
        if pid != pid:
            raise RuntimeError("os.
