import signal
# Test signal.setitimer() and signal.getitimer()

def alarm_handler(signum, frame):
    print 'alarm!'
    print 'signal', signum
    print 'frame', frame

signal.signal(signal.SIGALRM, alarm_handler)
signal.setitimer(signal.ITIMER_REAL, 0.1)
time.sleep(0.5)
print 'before', signal.getitimer(signal.ITIMER_REAL)
signal.setitimer(signal.ITIMER_REAL, 0.1)
time.sleep(0.5)
print 'after', signal.getitimer(signal.ITIMER_REAL)
</code>
prints
<code>before (0.0, 0.0)
after (0.0, 0.0)
alarm!
signal 14
frame &lt;frame object at 0xb7f2df9c&gt;
alarm!
signal 14
frame &lt;frame object at 0xb7f2df9c&gt;
</code>
