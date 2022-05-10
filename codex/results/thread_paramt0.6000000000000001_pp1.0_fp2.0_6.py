import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 2\n')).start()

# To run the thread, start() must be called.
#
# In the example above, the sys.stdout.write() function is passed to the target
# parameter of the Thread class.
#
# In this example, the thread stops before the main program ends. Because of
# this, the message "Hello from thread" is not displayed.
#
# To wait for the thread to finish, you can use the join() method.
#
# Example
# Wait for the thread to finish:

import threading
import time

def myfunction():
    print("Hello from a thread!")

mythread = threading.Thread(target=myfunction)
mythread.start()
mythread.join()

# The join() method blocks the calling thread (in this case the main program)
# until the thread whose join() method is called terminates
# (either normally or through an unhandled exception), or until the
