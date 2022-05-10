import signal
# Test signal.setitimer() and signal.signal()
#
# Notes:
# - This test will probably only work on posix systems, but that's ok
#   since it's not run on non-posix systems.
# - The test assumes that the signal handler is called exactly once for
#   each alarm.
# - The test currently does not check whether signal handlers are called
#   at the right time, only whether they are called at all.

import signal

SIG = signal.SIGALRM

def handler_1(signum, frame):
	pass

def handler_2(signum, frame):
	global num_2
	num_2 += 1

def handler_3(signum, frame):
	global num_3
	num_3 += 1

def handler_4(signum, frame):
	global num_4
	num_4 += 1

def test_signal():
	global num_2, num_3, num_4
	num_2 = num_3 = num_4 = 0

	# test signal.signal()
	signal.signal(
