import signal
# Test signal.setitimer
#
# From APUE:
# The following program demonstrates the use of setitimer to generate a
# SIGALRM signal once a second. It also illustrates the use of the SA_RESTART
# flag with sigaction so that read doesn't fail when the SIGALRM signal is
# caught.
import sys
import time

def handler(signum, frame):
    print time.ctime(), 'Alarm in', frame.f_code.co_name

def sig_alrm(sec):
    time.sleep(sec)
    print 'SIGALRM!'

def main():
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(2)
    sig_alrm(1)

if __name__ == '__main__':
    main()
