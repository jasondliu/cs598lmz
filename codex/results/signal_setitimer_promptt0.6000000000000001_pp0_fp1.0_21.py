import signal
# Test signal.setitimer
#
# (C)2003-2004 Chris Liechti <cliechti@gmx.net>
# this is distributed under a free software license, see license.txt

import time

def sigalarm(signum, frame):
    print("alarm!", time.time())

print("setitimer")
signal.signal(signal.SIGALRM, sigalarm)
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)

print("sleep")
time.sleep(2)

print("pause")
signal.pause()
