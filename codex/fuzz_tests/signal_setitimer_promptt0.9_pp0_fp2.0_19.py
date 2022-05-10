import signal
# Test signal.setitimer
interval = 3
signal.setitimer(signal.ITIMER_REAL, interval)
i = 1
while True:
    time.sleep(0.1)
    print i
    i += 1
</code>
The execution stops after 3 seconds :
<code>1
2
3
</code>
I do not understand why.


A:

You need to catch the signal for this to work the way you expect.
<code>def stop(signal_num, stack):
    printf("Signal %s received!", signal_num)
    exit(0)

signal.signal(signal.SIGALRM, stop)
</code>

