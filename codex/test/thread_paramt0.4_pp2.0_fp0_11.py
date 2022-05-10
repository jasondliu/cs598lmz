import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Thread started\n')).start()

import time
time.sleep(2.0)

print('Main thread exiting.')

# Thread started
# Main thread exiting.
