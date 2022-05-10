import signal
# Test signal.setitimer()
def setitimer_handler(signum, frame):
    print 'setitimer_handler'

signal.signal(signal.SIGALRM, setitimer_handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
for i in xrange(2):
    print 'setitimer process'
    time.sleep(2)
print 'setitimer process end'
while True:
    time.sleep(1)

# Test signal.set_wakeup_fd()
# def wakeupfd_handler(signum, frame):
#     print 'wakeupfd_handler'
# signal.signal(signal.SIGHUP, wakeupfd_handler)
# signal.set_wakeup_fd(signal.SIGHUP)
# print 'wakeupfd process'
# time.sleep(1)
# for i in xrange(10):
#     os.write(signal.SIGHUP, '1')
#     print 'wakeupfd process'
#     time.sleep(
