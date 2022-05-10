import signal
# Test signal.setitimer()
def setitimer_handler(num, frame):
	print("setitimer_handler:", num, frame)

signal.signal(signal.SIGALRM, setitimer_handler)
signal.setitimer(signal.ITIMER_REAL, 1, 0)
#signal.setitimer(signal.ITIMER_REAL, 1, 0.5)

# Test signal.signal()
#def signal_handler(num, frame):
#	print("signal_handler:", num, frame)

#signal.signal(signal.SIGINT, signal_handler)

# Test signal.getsignal()
#print(signal.getsignal(signal.SIGALRM))

# Test signal.set_wakeup_fd()
#fd = os.open("/path/to/file", os.O_WRONLY | os.O_APPEND)
#signal.set_wakeup_fd(fd)
#signal.set_wakeup_fd(fd, 1)


