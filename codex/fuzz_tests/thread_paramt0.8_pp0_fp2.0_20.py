import sys, threading
threading.Thread(target=lambda: sys.stdout.write('.')).start()

print 'a'
print 'b'
print 'c'

import time
time.sleep(1)

print 'e'
print 'f'
print 'g'
