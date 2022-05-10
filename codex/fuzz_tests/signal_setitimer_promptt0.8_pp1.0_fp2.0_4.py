import signal
# Test signal.setitimer() and signal.setitimer()
def timeout_handler(signum, frame):
    print("Time out!")
    raise

# install the signal.SIGALRM handler
signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(10)

# do what you want to do here
#time.sleep(15)

# reset the alarm
signal.alarm(0)

# call setitimer() to establish a new timer
signal.setitimer(signal.ITIMER_REAL,10)
time.sleep(15)
print("end")
# call setitimer() with 0 as the interval to disbale the timer
signal.setitimer(signal.ITIMER_REAL,0)
