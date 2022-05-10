import signal
# Test signal.setitimer()

def handler(signum, frame):
    print('Signal handler called with signal', signum)
    raise OSError("Couldn't open device!")

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

signal.setitimer(signal.ITIMER_REAL, 0)
# Do some other stuff
os.close(fd)

# 
# signal_alarm.py
# 
import signal
import time

def receive_alarm(signum, stack):
    print('Alarm :', time.ctime())

# Call receive_alarm in 2 seconds
signal.signal(signal.SIGALRM, receive_alarm)
signal.alarm(2)

print('Before:', time.ctime())
time.
