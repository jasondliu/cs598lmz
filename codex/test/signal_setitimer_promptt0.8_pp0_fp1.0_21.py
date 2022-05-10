import signal
# Test signal.setitimer

import os, time, sys
if sys.platform != "win32":
    setitimer = signal.setitimer
    ITIMER_REAL = signal.ITIMER_REAL
    ITIMER_VIRTUAL = signal.ITIMER_VIRTUAL
    ITIMER_PROF = signal.ITIMER_PROF

    def printtime():
        print('  time =', time.time())

    def alarm_handler(signum, frame):
        #print('Alarm!')
        printtime()

    def profiling_handler(signum, frame):
        #print('Profiling!')
        pass

    def wait_for_alarm(delay):
        #print('Sleeping for', delay, 'seconds')
        time.sleep(delay)
        #print('Awake!')


    def testit(which):
        #print('\nTimer', which)

        # Get the existing timer settings
        delay = 1
        odelay = delay / 2.0
        printtime()
        old = setitimer(which, odelay)

