import signal
# Test signal.setitimer() and signal.getitimer()

def handler(signum, frame):
    print('Signal handler called with signal', signum)

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

signal.alarm(5)           # Set the alarm again

print('Sleeping')
time.sleep(2)
print('Done')

# 这个程序打开一个终端设备，但是有一个5秒的超时。
# 如果超时发生，open() 会被中断，并且程序会继续执行。
#
