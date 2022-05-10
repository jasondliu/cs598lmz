import threading
# Test threading daemon
# https://stackoverflow.com/questions/190010/daemon-threads-explanation

def f():
    print('thread function')
    return

if __name__ == '__main__':
    for i in range(3):
        t = threading.Thread(target=f)
        t.setDaemon(True)
        t.start()
    main_thread = threading.currentThread()
    for t in threading.enumerate():
        if t is main_thread:
            continue
        print(t.getName())
        t.join()

# thread function
# Thread-1
# Thread-2
# Thread-3

# https://stackoverflow.com/questions/190010/daemon-threads-explanation

import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

def n():
    logging.debug('Starting')
    logging.debug('Exiting')

