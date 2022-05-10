import signal
# Test signal.setitimer(),etc.
period = 0.25

def handler(signum, frame):
    print "Got alarm", signum

# Set itimer
for i in [signal.ITIMER_REAL, # Decrements sys.time()
          signal.ITIMER_VIRTUAL, # Decrements process time
          signal.ITIMER_PROF]: # Decrements both
    print "Testing", i
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(i, period)
    time.sleep(2)
    signal.alarm(0) # Disable itimer

# This exits with code 1 because of the signal
print "This is the end"
</code>
Test it on Ubuntu 16.04 Python 2.7.12 and launch it from a terminal to see the output, you will get a traceback:
<code>python test_signal.py
Testing 0
Testing 1
Testing 2
Got alarm 14
Got alarm 14
Got alarm 14
Got alarm 14
Got alarm 14
Got alarm 14
Got alarm 14
Got alarm 14
Got alarm
