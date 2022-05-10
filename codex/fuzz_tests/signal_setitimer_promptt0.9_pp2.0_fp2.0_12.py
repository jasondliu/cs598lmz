import signal
# Test signal.setitimer(signal.ITIMER_REAL, 0, 0) without blocking
class TimeoutException(Exception): 
	pass 

def timeout_handler(signum, frame):
    raise TimeoutException("Timed out!")
    
signal.signal(signal.SIGALRM, timeout_handler)
signal.setitimer(signal.ITIMER_REAL, 0, 0.00001) # Set timeout of 1 microsecond
try:
    print("Processing...")
    s = 0
    while True:
        s += 1
except TimeoutException:
    print("Timed out!")
signal.setitimer(signal.ITIMER_REAL, 0, 0) # Disable the alarm
print("Done!")
