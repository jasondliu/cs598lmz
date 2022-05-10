import signal
# Test signal.setitimer support, to be called by test_signal.py
# which has the global try/except

sa = signal.SIGALRM
def handler(*args):
	pass
def no_intr_sleep(sec):
	# Sleep without signal interruptions
    old = signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, sec)
    pause()
    signal.setitimer(signal.ITIMER_REAL, 0)
    signal.signal(signal.SIGALRM, old)

def alarm_handler(*args):
	pass
def alarm_unavailable():
	"""Do the alarm test anyway, but with a small max loop count.

	The platform either has no SIGALRM, or some other problem
	making the test impractical.
	"""
	return no_intr_sleep(120)

