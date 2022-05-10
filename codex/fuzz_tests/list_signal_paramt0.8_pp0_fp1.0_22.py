import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(
            signal.ITIMER_REAL,
            delays.pop())

def job_func(x, y):
    return x+y

def main():
    for i in range(N):
        signal.setitimer(
            signal.ITIMER_REAL,
            delays.pop())
        started = datetime.now()
        x, y = random.randint(0, 100), random.randint(0, 100)
        # results.append(job_func(x, y))
        print(x, y, job_func(x, y))
        time_elapsed = datetime.now() - started
        print('Time elapsed (hh:mm:ss.ms) {}\n'.format(time_elapsed))

if __name__ == '__main__':
    main()
