import signal
# Test signal.setitimer before and after sleep
# Other kinds of alarms, either default or custom
# Get one alarm to go off while we sleep to see if this gets handled correctly
import os

def clock_handler(signal, frame):
	sys.stdout.write("\a")
	signal.setitimer(ITIMER_REAL, 1, 1)


signal.signal(signal.SIGALRM, clock_handler)
signal.setitimer(ITIMER_REAL, 1, 1)

while True:
	data = sys.stdin.read(1)

	if not data:
		break
	sys.stdout.write("\b \b")
	if data == '!':
		break
