import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

while delays:
    signal.pause()

# @pep8
# def example():
#     print('start')
#     import time
#     time.sleep(1)
#     print('end')
#
#
# def alarm_handler(signum, frame):
#     import random
#     delay = random.random() / 300.0
#     signal.setitimer(signal.ITIMER_REAL, delay)
#     example()
#
#
# def main():
#     signal.signal(signal.SIGALRM, alarm_handler)
#     signal.setitimer(signal.ITIMER_REAL, 0.1)
#     while True:
#         signal.pause()
#
#
# if __name__ == '__main__
