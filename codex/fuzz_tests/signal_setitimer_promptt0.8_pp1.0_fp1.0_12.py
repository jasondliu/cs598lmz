import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 1, 1)

# This sets the CPU time limit to 1 second.
signal.setitimer(signal.ITIMER_VIRTUAL, 1, 1)

# This sets the elapsed time limit to 1 second.
signal.setitimer(signal.ITIMER_PROF, 1, 1)

# This sets the wall-clock limit to 1 second.
# NOTE: This sets all limits at once.
signal.setitimer(signal.ITIMER_MONOTONIC, 1, 1)

# This sets the wall-clock limit to 1 second.
signal.setitimer(signal.ITIMER_MONOTONIC, 1, 1)

# This sets the process limit to 1 second.
signal.setitimer(signal.ITIMER_PROCESS, 1, 1)

# Get interval value for ITIMER_VIRTUAL
signal.getitimer(signal.ITIMER_VIRTUAL)

# Get interval value for IT
