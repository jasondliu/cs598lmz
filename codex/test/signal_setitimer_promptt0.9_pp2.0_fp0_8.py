import signal
# Test signal.setitimer()


import os, signal
signal.setitimer(signal.ITIMER_VIRTUAL, 1, 0)
# ...
pid = os.fork()
