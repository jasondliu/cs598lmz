import signal
# Test signal.setitimer
paused = False

def signal_handler(sig, frame):
    global paused
    if paused:
        print "Resuming!"
        paused = False
    else:
        print "Pausing!"
        paused = True
signal.signal(signal.SIGALRM, signal_handler)
signal.setitimer(signal.ITIMER_REAL, 0, 5)
while True:
    x = raw_input("")
    if x == "pause":
        signal.pause()
    elif x == "resume":
        signal.alarm(0)
    else:
        break
signal.setitimer(signal.ITIMER_REAL, 0, 0)
</code>

