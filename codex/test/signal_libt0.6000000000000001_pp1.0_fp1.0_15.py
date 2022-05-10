import signal
signal.signal(signal.SIGINT, signal_handler)

while True:
	time.sleep(1)
