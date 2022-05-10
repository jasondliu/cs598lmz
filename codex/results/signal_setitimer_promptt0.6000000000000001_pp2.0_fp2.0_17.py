import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("Got signal", signum)

# Set the timer to go off in 2 seconds
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 2)

# Do something else
while True:
    print("doing something")
 
# The above code will print the message "doing something" about every 0.1 seconds.
# After 2 seconds, the SIGALRM handler will be invoked, and the program will terminate.
