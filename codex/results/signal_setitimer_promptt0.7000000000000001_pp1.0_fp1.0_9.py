import signal
# Test signal.setitimer()
# from lembrar import lembrar


class timer:
    def __init__(self):
        self.start_time = 0
        self.end_time = time.time()

        self.stop_time = time.time()
        self.end_time = time.time()


def set_timer(seconds):
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, seconds)


def handler(signum, frame):
    print('I am being called')


def main():
    print('Program start')

    set_timer(5)
    signal.pause()

if __name__ == '__main__':
    main()
