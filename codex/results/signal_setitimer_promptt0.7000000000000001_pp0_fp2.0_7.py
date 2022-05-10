import signal
# Test signal.setitimer()

def signal_handler(signum, frame):
    print "Signal handler called with signal", signum
    raise IOError("Couldn't open device!")

signal.signal(signal.SIGALRM, signal_handler)
signal.setitimer(signal.ITIMER_REAL, 1)

print "Starting"
while True:
    print "Looping"

# Output:
# Starting
# Looping
# Looping
# Looping
# Looping
# Looping
# Looping
# Looping
# Looping
# Looping
# Looping
# Looping
# Looping
# Looping
# Looping
# Looping
# Looping
# Looping
# Looping
# Looping
# Looping
# Looping
# Looping
# Looping
# Looping
# Looping
# Looping
# Looping
# Looping
# Looping
# Looping
# Looping
# Looping
# Looping
# Looping
# Looping
# Looping
# Looping
# Looping
