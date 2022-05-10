import signal
# Test signal.setitimer
import multiprocessing
import time

def handler(signum, frame):
    pass

def run():
    it = multiprocessing.get_context('spawn').Process(target=loop)
    it.start()
    # let it start up
    time.sleep(0.1)
    signal.setitimer(signal.ITIMER_VIRTUAL, 0.5, 0.5)
    it.join()

def loop():
    while True:
        time.sleep(1)

signal.signal(signal.SIGVTALRM, handler)
run()
