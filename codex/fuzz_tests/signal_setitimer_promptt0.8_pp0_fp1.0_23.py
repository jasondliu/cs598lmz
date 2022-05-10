import signal
# Test signal.setitimer

def sig_alarm(signum,frame):
    global count
    count +=1
    if count % 10 == 0:
        print count,"seconds elapsed"

signal.signal(signal.SIGALRM,sig_alarm)

count = 0
# generate SIGALRM every 100 millseconds
signal.setitimer(signal.ITIMER_REAL,0.1,0.1)

while 1:
    time.sleep(1)
