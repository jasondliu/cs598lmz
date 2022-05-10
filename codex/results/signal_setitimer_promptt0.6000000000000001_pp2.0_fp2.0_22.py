import signal
# Test signal.setitimer() and signal.getitimer()
def handler(num, stack):
    print ("Received signal", num)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.2, 0.2)

# This will also block SIGALRM
print ("My PID is", os.getpid())
input()
