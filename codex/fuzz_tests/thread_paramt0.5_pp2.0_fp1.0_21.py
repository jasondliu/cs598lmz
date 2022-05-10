import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 2\n')).start()

# This is a bit of a hack, but it works fine.
# The output is not guaranteed to appear in any specific order.

# Hello from thread 1
# Hello from thread 2

# For example, the following is also a valid output:

# Hello from thread 2
# Hello from thread 1


# ----------------------------------------------------------------------------------------------------------------------
# Example 2:
# ----------------------------------------------------------------------------------------------------------------------

import threading

def thread_function(name):
    print("Thread %s: starting" % name)
    x = 0
    while x < 100:
        x += 1
    print("Thread %s: finishing" % name)

if __name__ == "__main__":
    print("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    print("Main    : before running thread")
    x.start()
    print("Main   
