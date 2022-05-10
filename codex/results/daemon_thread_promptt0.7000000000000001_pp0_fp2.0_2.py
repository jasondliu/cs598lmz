import threading
# Test threading daemon
# https://pymotw.com/2/threading/

import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

def daemon():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()
# Test process
# http://www.pythoncentral.io/introduction-to-python-threads/

from multiprocessing import Process
import threading

def print_func(continent='Asia'):
    print('The name of continent is : ', continent)
