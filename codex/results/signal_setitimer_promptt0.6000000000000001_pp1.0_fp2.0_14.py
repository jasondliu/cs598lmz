import signal
# Test signal.setitimer()

import signal, os

# Receives the signal and prints which one
def signal_handler(signum, frame):
    print 'Received signal', signum

# Register the signal_handler function to respond to the signal.signal(signum, handler)
# signal.SIGALRM is the signal that is sent to a process when its time limit expires
signal.signal(signal.SIGALRM, signal_handler)

# setitimer(which, seconds, interval=0)
# which = ITIMER_REAL: decrements for every real-time second
#         ITIMER_VIRTUAL: decrements when the process is executing.
#         ITIMER_PROF: decrements when the process is executing and when the system is running on behalf of the process.
# seconds = interval at which a signal is sent to the process
# interval = interval at which a signal is sent to the process
signal.setitimer(signal.ITIMER_REAL, 1)

print 'Before:', signal.getitimer(signal.ITIMER_REAL)
