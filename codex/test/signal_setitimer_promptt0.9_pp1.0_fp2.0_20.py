import signal
# Test signal.setitimer
# setitimer(which, seconds, interval)
# which: ITIMER_REAL,ITIMER_VIRTUAL,ITIMER_REAL,ITIMER_PROF
# interval: 0 -- ITIMER_ONCE

signal.setitimer(signal.ITIMER_REAL,1,0)

