import threading
# Test threading daemon
import time
# Test time
import random
# Test random
import sys
# Test sys
import os
# Test os

# Test logging
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

# Test threading
def worker(num):
    """thread worker function"""
    logging.debug('Starting')
    time.sleep(0.2)
    logging.debug('Exiting')

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

# Test time
start = time.time()
time.sleep(random.random() * 2)
print("--- %s seconds ---" % (time.time() - start))

# Test sys
print(sys.version)
print(sys.version_info)
print(sys.platform)
print(sys.argv)

# Test os
print(os.name)
print
