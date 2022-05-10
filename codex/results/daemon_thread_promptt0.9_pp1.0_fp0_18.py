import threading
# Test threading daemon

import threading
import logging
logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s',)

def daemon():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')

def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()

# https://pymotw.com/3/threading/index.html
# In a multithreaded context, Daemon threads are slated for termination
# when the main thread [or whoever is the parent thread] finishes execution.
# With their  parent thread gone, daemon threads are no longer considered useful
# and the Python interpreter exits them automatically. If any daemon threads
# remain alive
