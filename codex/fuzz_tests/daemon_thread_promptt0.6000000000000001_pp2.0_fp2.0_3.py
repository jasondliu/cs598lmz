import threading
# Test threading daemon
def daemon():
    print('Starting')
    time.sleep(0)
    print('Exiting')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print('Starting')
    print('Exiting')

t = threading.Thread(name='non-daemon', target=non_daemon)

# d.start()
# t.start()
# d.join(1)
# print('d.isAlive()', d.isAlive())
# t.join()

# Deadlock
import threading
import logging
import time

def lock_holder(lock):
    logging.debug('Starting')
    while True:
        lock.acquire()
        try:
            logging.debug('Holding')
            time.sleep(0.5)
        finally:
            logging.debug('Not holding')
            lock.release()
        time.sleep(0.5)
    return

def worker(lock):
    logging.debug('Starting')

