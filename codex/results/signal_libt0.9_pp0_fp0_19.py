import signal
signal.signal(signal.SIGHUP, signal_handler)
while True:
    time.sleep(0.2)
