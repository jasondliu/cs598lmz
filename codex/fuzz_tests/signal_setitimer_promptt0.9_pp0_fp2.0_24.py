import signal
# Test signal.setitimer, and main

import support

(numcalls, alarmtime) = (0, 0)

def handler(signum, frame):
    global numcalls, alarmtime
    numcalls = numcalls + 1
    alarmtime = alarmtime + support.SAMPLE_DELAY

signal.signal(signal.SIGALRM, handler)

starttime = time.time()
signal.setitimer(signal.ITIMER_REAL, 0.2, support.SAMPLE_DELAY)
time.sleep(1.0)
signal.setitimer(signal.ITIMER_REAL, 0, 0)

endtime = time.time()

try:
    support.compare(numcalls != 0, 1)
except:
    pass
else:
    print 'Handlers were called too many times'

runtime = endtime - starttime
support.compare(abs(runtime - alarmtime), 0.2)
