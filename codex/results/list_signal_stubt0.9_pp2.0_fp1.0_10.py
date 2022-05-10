import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        logger.info("%d signals completed.", N)
        raise SystemExit


if __name__ == '__main__':
    import logging
    logger = logging.getLogger('main')
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG)

    signal.signal(signal.SIGALRM, handler)
    handler()

    min_delay = min(delays)
    print("min delay = %g s." % min_delay)
    delay = min_delay * 2
    print("using delay = %g s." % delay)

    log_signals = True
    while True:
        elapsed = time.perf_counter()
        signal.setitimer(signal.ITIMER_REAL, delay)
        if log_signals:
            logger.debug("Waiting for signal.")
        time.sleep(1e-4) # I'm not sure why I need to do this.
        elapsed = time.perf_counter() - elapsed
        if log_signals:
           
