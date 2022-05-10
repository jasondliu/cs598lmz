import sys, threading
threading.Thread(target=lambda:
    sys.stdin.readline()
).start()

#make a time series
import numpy as np
import time

test_values = list(np.arange(10))
for value in test_values:
    ts = time.time()
    print(value, ts)
    time.sleep(1)
