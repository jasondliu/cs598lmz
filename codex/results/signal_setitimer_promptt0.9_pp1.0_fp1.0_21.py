import signal
# Test signal.setitimer
#
# Declare the signal handler
signal.signal(signal.SIGALRM, timer_expired)


timer_counter = 0

# Set the timer to go off in 1 second
signal.setitimer(signal.ITIMER_REAL, 1, 0)


while True:
    print('The alarm has not gone off yet, this program will be stuck for 1 second')
    time.sleep(1)
    print('Hello')
