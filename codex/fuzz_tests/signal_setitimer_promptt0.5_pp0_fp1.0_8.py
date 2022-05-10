import signal
# Test signal.setitimer
import signal as s

def handler(signum, frame):
    print("signum:", signum)

s.setitimer(s.ITIMER_VIRTUAL, 0.1, 0.1)
s.signal(s.SIGVTALRM, handler)

# Test signal.set_wakeup_fd
import signal as s

def handler(signum, frame):
    print("signum:", signum)

s.set_wakeup_fd(1)
s.signal(s.SIGUSR1, handler)

# Test signal.siginterrupt
import signal as s

def handler(signum, frame):
    print("signum:", signum)

s.signal(s.SIGINT, handler)
s.siginterrupt(s.SIGINT, True)

# Test signal.sigpending
import signal as s

def handler(signum, frame):
    print("signum:", signum)

s.signal(s.SIGUSR1, handler)

