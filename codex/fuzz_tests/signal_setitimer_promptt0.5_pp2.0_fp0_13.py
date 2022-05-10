import signal
# Test signal.setitimer() and signal.getitimer()


def handler(signum, frame):
    print("Time's up!")


signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 2)

while True:
    print('Tick')
    time.sleep(1)

# Test signal.setitimer() and signal.getitimer()
# https://docs.python.org/3/library/signal.html
# The setitimer() function is a thin wrapper around the system call of the same name. The getitimer() function is a thin wrapper around the system call of the same name.
#
# The setitimer() function sets the timer specified by which to the new value specified by the itimer structure pointed to by new_value.
#
# The getitimer() function returns the current value of the timer specified by which in the itimer structure pointed to by old_value.
#
# The itimer structure is defined as follows:
#
# struct itimerval {
#     struct timeval it_
