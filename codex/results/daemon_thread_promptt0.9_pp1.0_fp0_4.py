import threading
# Test threading daemon
def daemon():
    print('Start daemon...')
    time.sleep(3)
    print('End daemon...')

def non_daemon():
    print('Start non daemon...')
    print('End non daemon...')

d = threading.Thread(name = 'daemon', target = daemon)
d.setDaemon(True) # daemon will always terminate after program finishes executing

t = threading.Thread(name = 'non daemon', target = non_daemon)

d.start()
t.start()

d.join()
t.join()

import logging

logging.basicConfig(level = logging.DEBUG, format = '%(threadName)s: %(message)s')

def worker1():
    logging.debug('Starting')
    time.sleep(2)


def worker2():
    logging.debug('Starting')
    time.sleep(2)

def worker3():
    logging.debug('Starting')
    time.sleep(2)

t = threading.Thread(target = worker1)
t.setDaemon(
