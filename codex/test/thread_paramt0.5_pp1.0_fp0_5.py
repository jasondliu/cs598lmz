import sys, threading
threading.Thread(target=lambda: sys.stdout.write('.')).start()
from time import sleep
sleep(0.1)
print('done')

# This is a more advanced example of the same technique,
# which allows you to pass arguments to the thread.
import sys, threading
threading.Thread(target=lambda: sys.stdout.write('.'), args=()).start()
from time import sleep
sleep(0.1)
print('done')

# This is a more advanced example of the same technique,
# which allows you to pass arguments to the thread.
import sys, threading
threading.Thread(target=lambda: sys.stdout.write('.'), args=(), kwargs={}).start()
from time import sleep
sleep(0.1)
print('done')

# This is a more advanced example of the same technique,
# which allows you to pass arguments to the thread.
import sys, threading
threading.Thread(target=lambda: sys.stdout.write('.'), args=(), kwargs={'x': 1}).start()
from time import sleep
