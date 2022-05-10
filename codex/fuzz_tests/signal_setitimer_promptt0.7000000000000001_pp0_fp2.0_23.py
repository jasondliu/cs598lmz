import signal
# Test signal.setitimer()
def handler(signum, frame):
    print "got it"
    raise Exception("got it")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

print "here"
try:
    for i in range(10):
        sleep(1)
        print i
except:
    print "exception"

print "done"


# Test signal.set_wakeup_fd()
# def alarm_handler(signum, frame):
#     print "got it"
#     raise Exception("got it")

# signal.signal(signal.SIGALRM, alarm_handler)
# signal.setitimer(signal.ITIMER_REAL, 5)
# wfd = os.open("/dev/null", os.O_WRONLY)
# signal.set_wakeup_fd(wfd)

# print "here"
# try:
#     for i in range(10):
#         sleep(1)
#        
