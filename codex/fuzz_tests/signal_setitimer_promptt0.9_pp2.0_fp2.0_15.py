import signal
# Test signal.setitimer() here
import sys


def make_report():
    ...


def handler(num, frame):
    print(f'{num}: {frame}')
    # setitimer() example:
    # https://docs.python.org/3/library/signal.html#signal.setitimer
    ret_value = 0 - sys.getrefcount(frame)
    if num == signal.SIGALRM:
        print('One hour has passed...')
        make_report()
    print(f'The refcount of frame is {ret_value}')
    # res = sys.getrefcount(frame)
    sys.exit(0)


def main():
    signal.signal(signal.SIGALRM, handler)
    # alarm(int(os.environ.get('TEST_INTERVAL', 60)))
    signal.setitimer(signal.ITIMER_REAL, 1, 1)  # Start 1 second, reset every 1 second after.
    for i in range(100000):
        print(i)
        time.sleep(1
