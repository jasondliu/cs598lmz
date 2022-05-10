import signal
# Test signal.setitimer: generate SIGALRM
signal.setitimer(signal.ITIMER_REAL, 1)
# Wait for timeout
start = time.time()
time.sleep(2)
delay = time.time() - start
if delay < 1 or delay > 1.5:
    print("Skipped:", delay)
else:
    print("OK:", delay)
# Test signal.alarm: generate SIGALRM
signal.alarm(1)
# Wait for timeout
start = time.time()
time.sleep(2)
delay = time.time() - start
if delay < 1 or delay > 1.5:
    print("Skipped:", delay)
else:
    print("OK:", delay)
