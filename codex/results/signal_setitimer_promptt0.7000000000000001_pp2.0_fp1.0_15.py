import signal
# Test signal.setitimer()

def alarm_handler(signum,frame):
    print("Alarm called at: ", time.ctime())
    time.sleep(5)
    print("Alarm finished at: ", time.ctime())

# Register the signal function handler
signal.signal(signal.SIGALRM,alarm_handler)

# Set the timer
signal.setitimer(signal.ITIMER_REAL,1,2)
time.sleep(20)

print("The current time is : ", time.ctime())
