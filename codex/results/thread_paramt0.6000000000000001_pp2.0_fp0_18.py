import sys, threading
threading.Thread(target=lambda: sys.stdout.write('my output\n')).start()

# %%
# Switching from one thread to another is done by the operating system,
# not by Python.
#
# When a thread exits, its thread identifier can be reused for another thread.
#
# A thread can get its own identifier by calling threading.get_ident().

# %%
# The following code runs the function target in a separate thread,
# and prints the thread identifier in the main thread.

import threading

def target():
    print('Thread running')

thread = threading.Thread(target=target)
thread.start()
print(thread.ident)

# %%
# Threads communicate using shared objects.
#
# Each object has a lock that must be held by the current thread
# before it can read or write the object's attributes.

# %%
# When an object is created, its lock is unlocked.
#
# When the lock is locked, subsequent attempts to lock it block
# until it is unlocked, then lock it and return.
#
# When the lock is unlocked, it must be held
