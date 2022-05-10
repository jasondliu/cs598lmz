import signal
# Test signal.setitimer()
#
# @TODO: Test the itimerval structure (unix)
#
# Test cases:
#
# 1. Test signal.setitimer()
# 2. Test signal.setitimer() with SIGALRM
# 3. Test signal.setitimer() with SIGVTALRM
# 4. Test signal.setitimer() with SIGPROF
#
signal.setitimer(signal.ITIMER_REAL, 0.001, 0.001)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.001, 0.001)
signal.setitimer(signal.ITIMER_PROF, 0.001, 0.001)

# Test signal.getitimer()
#
# @TODO: Test the itimerval structure (unix)
#
# Test cases:
#
# 1. Test signal.getitimer()
# 2. Test signal.getitimer() with SIGALRM
# 3. Test signal.getitimer() with SIGVTALRM
# 4. Test signal.
