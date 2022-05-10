import signal
# Test signal.setitimer()
def handletimer(signum, frame):
    # print 'Alarm :', time.ctime()
    print 'handletimer'
    signal.alarm(3)


print 'Before :', time.ctime()
signal.signal(signal.SIGALRM, handletimer)
signal.alarm(3)

time.sleep(4)
print 'After :', time.ctime()
