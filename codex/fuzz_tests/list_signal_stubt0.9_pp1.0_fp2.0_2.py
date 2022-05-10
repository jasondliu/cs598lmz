import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    print "Hi!"


def worker(fn, args, delay):
    signal.setitimer(signal.ITIMER_REAL, 1.0, 0.01)
    #signal.setitimer(signal.ITIMER_REAL, delays.pop())
    while delays:
        fn(*args)


def main():
    parser = OptionParser()
    parser.add_option("-j", "--jobs", default=1, type=int)
    (options, args) = parser.parse_args()

    main_fn = args[0]
    if '.' in main_fn:
        main_args = main_fn.split('.')
        main_args = (main_args[0], '.'.join(main_args[1:]))
    else:
        main_args = (main_fn, '')
    main_fn = importlib.import_module(*main_args)

    signal.signal(signal.SIGALRM, handler)
    if not main_fn.main:
        main_fn.main =
