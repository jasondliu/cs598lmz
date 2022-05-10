import signal
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
signal.sigwaitinfo((signal.SIGINT, signal.SIGTERM))
