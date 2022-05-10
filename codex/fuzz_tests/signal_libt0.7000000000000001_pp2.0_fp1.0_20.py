import signal
signal.signal(signal.SIGINT, signal_handler)

print('Press Ctrl+C')
signal.pause()
