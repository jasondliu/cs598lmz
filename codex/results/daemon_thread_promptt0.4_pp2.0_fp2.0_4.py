import threading
# Test threading daemon
# https://docs.python.org/3/library/threading.html

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

def f(name):
    logging.debug('starting')
    logging.debug('exiting')

if __name__ == '__main__':
    t = threading.Thread(name='non-daemon', target=f, args=('bob',))
    d = threading.Thread(name='daemon', target=f, args=('steve',))
    d.setDaemon(True)

    d.start()
    t.start()

    d.join()
    t.join()

# (daemon    ) starting
# (non-daemon) starting
# (daemon    ) exiting
# (non-daemon) exiting
