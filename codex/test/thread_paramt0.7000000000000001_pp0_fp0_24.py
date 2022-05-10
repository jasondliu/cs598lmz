import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\a')).start()

import time
time.sleep(1)

print('\a')
print('\a')

sys.stdout.write('\a')
sys.stdout.flush()

print('\007')
print('\a')

import os
os.system('\a')
