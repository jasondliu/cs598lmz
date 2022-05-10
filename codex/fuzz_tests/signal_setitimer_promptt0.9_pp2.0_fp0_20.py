import signal
# Test signal.setitimer, siginterrupt, signal.pause and signal.alarm

debug = False

def sigalrm(signum, frame):
    if not debug:
        pass
    else:
        print('sigalrm: signum=%d, frame=%s' % (signum, frame))

ITIME = 30, 5
itime1 = ITIME[0]  # time for setitimer
itime2 = ITIME[1]  # time for alarm

def start_timer(func, t):
    signal.signal(signal.SIGALRM, func)
    signal.setitimer(signal.ITIMER_REAL, t)
    print("Timer started for %d secs." % t)

# siginterrupt does not work on Windows,
# but it should not fail
if hasattr(signal, 'siginterrupt'):
    signal.siginterrupt(signal.SIGALRM, False)

# Start timer itime1 seconds
start_timer(sigalrm, itime1)

s = 0
while s <
