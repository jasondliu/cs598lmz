import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

import time
# Test time.sleep
time.sleep(0.2)

import thread
# Test thread.start_new_thread
def test():
    time.sleep(0.2)
thread.start_new_thread(test, ())

import threading
# Test threading.Thread
t = threading.Thread(target=test)
t.start()
t.join()

# Test threading.Timer
t = threading.Timer(0.2, test)
t.start()
t.join()
