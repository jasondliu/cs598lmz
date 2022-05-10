import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
        if delays:
            print(len(delays), 'left')
        else:
            print('done')

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

print('Starting loop')

while delays:
    signal.pause()

print('Loop terminated')

# Starting loop
# 9999 left
# 9998 left
# 9997 left
# 9996 left
# 9995 left
# 9994 left
# 9993 left
# 9992 left
# 9991 left
# 9990 left
# 9989 left
# 9988 left
# 9987 left
# 9986 left
# 9985 left
# 9984 left
# 9983 left
# 9982 left
# 9981 left
# 9980 left
# 9979 left
# 9978 left
# 9977 left
# 9976 left
# 9975 left
# 9974 left
# 9973 left
# 9972 left
# 9971 left
# 9970 left
# 9969
