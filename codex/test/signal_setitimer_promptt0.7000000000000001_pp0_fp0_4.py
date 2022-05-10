import signal
# Test signal.setitimer
import sys


def signal_handler(signum, frame):
    pass

signal.signal(signal.SIGALRM, signal_handler)
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)
# signal.alarm(1)
old_alarm_handler = signal.getsignal(signal.SIGALRM)
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)

signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)
old_alarm_handler = signal.getsignal(signal.SIGALRM)
try:
    f = open(sys.argv[0])
except OSError as e:
    print(e)

try:
    f = open('this_file_does_not_exist')
except OSError as e:
    print(e)
finally:
    print('Finally...')
