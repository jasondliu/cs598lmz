import signal
# Test signal.setitimer() out
signal.setitimer(signal.ITIMER_VIRTUAL, 3)
# Can also use signal.ITIMER_REAL and signal.ITIMER_PROF
# Note:
#   If a signal handler is not set, signals cause their
#   terminations by default. Therefore, the code below
#   will terminate within 3 seconds.
time.sleep(4)

import os
# Return the list of names of files in the nominated directory
#   based on the pathname argument you pass it
print(os.listdir('.'))
# To get the first script on the command-line
print(sys.argv[0])
