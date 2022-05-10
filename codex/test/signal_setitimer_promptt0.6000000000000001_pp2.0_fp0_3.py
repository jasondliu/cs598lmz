import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_PROF, 0.02, 0)

while True:
    time.sleep(1)
    print("Hello world")
