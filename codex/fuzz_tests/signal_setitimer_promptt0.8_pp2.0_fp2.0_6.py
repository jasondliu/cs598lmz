import signal
# Test signal.setitimer, signal.alarm
def handler(signum, frame):
    print("Time's up!")

signal.signal(signal.SIGALRM, handler)

# signal.alarm(5)
signal.setitimer(signal.ITIMER_REAL, 5, 0)

while True:
    signal.pause()

# Test timerfd
# import timerfd
# fd = timerfd.create(timerfd.CLOCK_MONOTONIC, timerfd.TFD_NONBLOCK)
# fd = timerfd.create(timerfd.CLOCK_REALTIME, timerfd.TFD_NONBLOCK)
# print(fd)
# timerfd.settime(fd, 5, 0)
# s = os.read(fd, 8)
# print(s)
# import os
# import select
# r, w, e = select.select([fd], [], [])
# print(r)
