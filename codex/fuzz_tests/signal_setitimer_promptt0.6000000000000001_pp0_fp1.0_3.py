import signal
# Test signal.setitimer()
#
# Should print "Alarm clock" every second
# until ctrl-C is pressed

def signal_handler(signum, frame):
    print("Alarm clock")

signal.signal(signal.SIGALRM, signal_handler)
signal.setitimer(signal.ITIMER_REAL, 1, 0.5)

while True:
    time.sleep(1)
    print("sleep 1 second")
