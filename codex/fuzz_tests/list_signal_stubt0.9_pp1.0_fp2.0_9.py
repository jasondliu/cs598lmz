import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        print('\nAll done')
        sys.exit(0)

def main():
    for delay in delays:
        signal.setitimer(signal.ITIMER_REAL, delay)
        try:
            exec('''
if 1:
    print(1)
    x = 1
''')
        except Exception:
  
