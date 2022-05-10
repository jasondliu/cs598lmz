import signal
# Test signal.setitimer(signal.ITIMER_PROF, 0.5);
# and exit after ~5 seconds...

def handler(signum, frame):
    print("signum: ", signum, " frame: ", frame)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_PROF, 0.5);
time.sleep(5)
signal.alarm(0)
</code>
However, when executing above code, I see this (i.e. 2 iterations):
<code>signum:  27  frame:  &lt;frame object at 0x2da9b78&gt;
signum:  27  frame:  &lt;frame object at 0x2da9b78&gt;
</code>
I would like to have the signal handler to print 5 times.
(I have read the manual and I have see similar questions here, but nothing seems to help).
Thanks.


A:

I believe what you want is to send SIGALRM to your process and handle this signal with your handler. By
