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

