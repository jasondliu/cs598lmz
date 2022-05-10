import signal
signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGTERM, handler)

