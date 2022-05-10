import sys, threading
threading.Thread(target=lambda: sys.stdout.write('.')).start()

import time
time.sleep(60)

print('Done')
