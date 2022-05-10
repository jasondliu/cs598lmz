import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    if delays:
        print('\last frame ended {:.3f}s late'.format(duration - frame_duration))

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

import IPython.display
import cv2

cap = cv2.VideoCapture(0)

while True:
    start = time.time()
    print('\r                                ', end='')
    print('\r')
    ret, img = cap.read()
    IPython.display.clear_output(wait=True)
    IPython.display.display(IPython.display.Image(data=cv2.imencode('.png', img)[1]))
    end = time.time()
    duration = end - start
    frame_duration = end - delay
    #print('\r{:.3f} {:.3f}'.format(duration, frame_duration), end='')
    #print('\r{:.3f}'.format(
