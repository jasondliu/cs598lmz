import signal
signal.setitimer(signal.ITIMER_REAL, 2, 2)
signal.pause(); print('ok')
