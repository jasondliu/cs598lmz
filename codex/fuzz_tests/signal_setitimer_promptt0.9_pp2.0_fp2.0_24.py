import signal
# Test signal.setitimer():

def alarm_handler(signum, frame):
    print("ALARM! wake up")

print("set alarm in 1.5 seconds")
signal.signal(signal.SIGALRM, alarm_handler)
signal.setitimer(signal.ITIMER_REAL, 1.5)
try:
    while True:
        print(".")
        time.sleep(0.5)
    print("done")
except KeyboardInterrupt:
    pass

print("Program complete")
