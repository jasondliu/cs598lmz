import signal
# Test signal.setitimer() by setting the alarm.
# 2016-11-23, Georg Fischer
#--------------------------------------------

INTERVAL = 0.08
signum   = signal.SIGALRM
handler  = signal.SIG_DFL

def main():
    # signal.signal(signum, handler)
    signal.setitimer(signum, INTERVAL, 0)
    cnt = 500
    sum = 0
    while cnt >= 0:
        sum += 1
        print(cnt, sum)
        # next timer signal
        signum, frame = signal.pause()
        cnt -= 1
#-----------
