import threading
# Test threading daemon
# You will need to stop the script manually with ctrl+C

import threading
import logging
import time

# Python daemon
class MyThread(threading.Thread):
    def run(self):
        logging.debug('running')
        time.sleep(5)
        logging.debug('done')

# Set up file for logging
logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

for i in range(3):
    t = MyThread()
    t.setDaemon(True)
    t.start()

# You should see all three threads exit
# after sleeping for 5 seconds.
main_thread = threading.currentThread()
for t in threading.enumerate():
    if t is main_thread:
        continue
    logging.debug('joining: %s', t.getName())
    t.join()
