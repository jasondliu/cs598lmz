import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        print "done"
        signal.signal(signal.SIGALRM, signal.SIG_IGN)

def signal_test():
    for i in range(N):
        signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, delays.pop())
    while delays:
        signal.pause()

print "signal test"
begin = time.time()
signal_test()
end = time.time()
print end - begin

def select_test():
    import select
    l = []
    for i in range(N):
        l.append(time.time())
    while l:
        delay = l[0] + delays.pop() - time.time()
        if delay > 0:
            select.select([], [], [], delay)
        else:
            l.pop(0)
    print "done"

print "select test"
begin = time.time()
select_test()
end = time.time()
print
