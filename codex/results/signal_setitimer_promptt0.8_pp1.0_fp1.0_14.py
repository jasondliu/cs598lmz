import signal
# Test signal.setitimer()
for i in range(5):
    # time.sleep(1)
    print(i)

def handler(signum, frame):
    print('Alarm :', time.ctime())

# signal.signal(signal.SIGALRM, handler)
# signal.alarm(5)
#
# signal.setitimer(signal.ITIMER_REAL, 5, 0)
# signal.setitimer(signal.ITIMER_VIRTUAL, 5, 0)
# signal.setitimer(signal.ITIMER_PROF, 5, 0)

def sig_usr1(signum, frame):
    print signum
    print frame
    print 'Received USR1'

signal.signal(signal.SIGUSR1, sig_usr1)
signal.signal(signal.SIGUSR2, sig_usr1)
print('My PID is:', os.getpid())

# while True:
#     print('Yawn...')
#     time.sleep(2)

