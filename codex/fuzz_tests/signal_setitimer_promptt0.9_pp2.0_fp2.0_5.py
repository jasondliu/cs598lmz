import signal
# Test signal.setitimer to schedule periodic alarms, and repeat a limited number
# of times.  Check the signal handler receives the right information (what the
# number of updates, and which type of timer was used).

def handler(signum, frame, count, what):
    print(signum, frame, count, what)
    frame.f_globals['exit'] = True

global exit
exit = False
signal.signal(signal.SIGALRM, handler)

for value in range(2):
    count = 0
    signal.setitimer(value, 1, 0)
    while not exit:
        signal.pause()
        count = count + 1
    exit = False
    signal.setitimer(value, 1, 1)
    while not exit:
        signal.pause()
    exit = False
    signal.setitimer(value, 0.2, 1)
    while not exit:
        signal.pause()

signal.setitimer(signal.ITIMER_REAL, 1, 0)

count = 0
handler(signal.SIGALRM
