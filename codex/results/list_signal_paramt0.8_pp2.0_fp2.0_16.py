import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
    else:
        print('Done!')
        exit(0)

signal.signal(signal.SIGALRM, handler)
handler()
#signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
while True:
    pass


# handler = lambda signum, frame: None
# signal.signal(signal.SIGALRM, handler)
#
# count = 0
# while True:
#     while True:
#         count += 1
#         if time.time() >= 1.0:
#             break
#
#     print(count)
#     count = 0
#     signal.setitimer(signal.ITIMER_REAL, 1.0)
