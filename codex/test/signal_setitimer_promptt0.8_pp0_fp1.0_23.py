import signal
# Test signal.setitimer

def sig_alarm(signum,frame):
    global count
    count +=1
