import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays[0])
        delays.pop(0)
        # print delays[0]
    else:
        os.kill(os.getpid(), signal.SIGKILL)
        print('signal.SIGKILL')
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays[0])

def long_term_sleep(secs):
    time.sleep(secs)

# def test():
#     print 'long_term_sleep', 1
#     sys.stdout.flush()
#     long_term_sleep(1)
#     print 'long_term_sleep', 0.5
#     sys.stdout.flush()
#     long_term_sleep(0.5)
#     print 'long_term_sleep', 2
#     sys.stdout.flush()
#     long_term_sleep(2)
#     print 'end'
#     sys.stdout.flush()

def main():
