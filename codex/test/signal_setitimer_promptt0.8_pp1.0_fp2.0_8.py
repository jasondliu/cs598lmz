import signal
# Test signal.setitimer() with every possible combination of the available
# constants -- signal.ITIMER_REAL, signal.ITIMER_VIRTUAL and
# signal.ITIMER_PROF.
import signal, sys
sys.path.insert(0, '..')

# Define some handler functions
def signal_handler(signal, frame):
    print("Signal handler called with signal: ", signal)

signal.signal(signal.SIGALRM, signal_handler)

# Now call signal.setitimer() for every possible combination of
# TIMERS -- real, virtual and prof.
for imode in range(3):
    for itimer in (signal.ITIMER_REAL, signal.ITIMER_VIRTUAL, signal.ITIMER_PROF):
        signal.setitimer(itimer, 1, 0)
        signal.pause()
        if itimer == signal.ITIMER_REAL:
            print("Time remaining for ITIMER_REAL: ", signal.getitimer(itimer))
