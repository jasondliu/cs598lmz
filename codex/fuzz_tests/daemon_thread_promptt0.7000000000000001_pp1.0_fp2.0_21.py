import threading
# Test threading daemon
def a_thread():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(3)
    print(threading.currentThread().getName(), 'Exiting')

def another_thread():
    t = threading.Timer(1, a_thread)
    t.setDaemon(True)
    t.start()
    print(threading.currentThread().getName(), 'Exiting')

if __name__ == '__main__':
    a_thread()
    another_thread()

# import logging
# logging.debug('Debug')
# logging.info('Info')
# logging.warning('Warning')
# logging.error('Error')
# logging.critical('Critical')
