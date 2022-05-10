import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        sys.exit(1)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

while True:
    print('.')
    if not delays:
        break
rpm = 0
n_digits = 5
for car in cars:
    rpm += car.rpm
rpm /= N
if rpm == 0:
    print('\nAll cars failed')
else:
    print(f'Total RPM = {round(rpm / N, n_digits)}')
len(cars)
for car in cars:
    car.destroy()
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
from
