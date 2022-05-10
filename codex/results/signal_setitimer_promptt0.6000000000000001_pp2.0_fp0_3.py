import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_PROF, 0.02, 0)

while True:
    time.sleep(1)
    print("Hello world")
</code>
Edit:
From the documentation of <code>signal.setitimer</code> it is clear that the timer is reset every time it expires.
<blockquote>
<p>If the timer expires and the handler function raises an exception,
  the timer will be reset to the initial value and restarted.</p>
</blockquote>

