import signal
# Test signal.setitimer
# The timer sets a flag which is checked in the main loop
#
def handler(signum, frame):
    global flag
    flag = True

def killer():
    global flag
    global killed
    killed = True
    flag = True

def main():
    global flag
    global killed

    # Catch SIGALRM
    signal.signal(signal.SIGALRM, handler)
    # Catch SIGTERM
    signal.signal(signal.SIGTERM, killer)

    # Set a timer to go off in 2 seconds
    signal.setitimer(signal.ITIMER_REAL, 2)

    # Main loop
    while True:
        if flag == True:
            if killed == True:
                print "SIGTERM received"
                break
            else:
                print "SIGALRM received"
                # Reset the flag
                flag = False
                # Set a timer to go off in 2 seconds
                signal.setitimer(signal.ITIMER_REAL, 2)
        time.sleep(1)

if __
