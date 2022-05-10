import signal
# Test signal.setitimer()

def timeout(unused_signo, unused_frame):
    raise RuntimeError("timeout")

signal.signal(signal.SIGALRM, timeout)
signal.setitimer(signal.ITIMER_REAL, 2, 0)
try:
    while True:
        pass
except RuntimeError:
    print("Timed out!")

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
