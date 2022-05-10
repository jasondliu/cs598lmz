import threading
# Test threading daemon
# import time
# import logging
# import random
# logging.basicConfig(level=logging.DEBUG,
#                     format='(%(threadName)-10s) %(message)s',
#                     )

# def daemon():
#     logging.debug('Starting')
#     time.sleep(2)
#     logging.debug('Exiting')

# def non_daemon():
#     logging.debug('Starting')
#     logging.debug('Exiting')

# d = threading.Thread(name='daemon', target=daemon)
# d.setDaemon(True)

# t = threading.Thread(name='non-daemon', target=non_daemon)

# d.start()
# t.start()
# Test threading stop

# import threading
# import time

# class ThreadingExample(object):
#     """ Threading example class
#     The run() method will be started and it will run in the background
#     until the application exits.
#     """

#     def __init__(self, interval=1
