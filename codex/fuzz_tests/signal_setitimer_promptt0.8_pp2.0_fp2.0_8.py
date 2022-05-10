import signal
# Test signal.setitimer(), that it is restricted to the main thread
# and that the alarm goes off in the main thread.
from threading import Thread

def handler_main():
    print('alarm in main thread')

signal.signal(signal.SIGALRM, handler_main)
thread = Thread(target=signal.setitimer, args=(signal.ITIMER_REAL, 1))
thread.start()
thread.join()
time.sleep(0.1)
signal.setitimer(signal.ITIMER_REAL, 0)
