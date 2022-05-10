import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from child')).start()
sys.stdout.write('Hello from parent')
 
# Output:
# Hello from parent
# Hello from child

# if we run this code, you will see that the parent thread writes its message first,
# but since the child thread is being run in the background, there is no telling
# in which order the messages will be printed.

# You will notice that the output is not exactly what we expected.
# In fact, it is quite mangled. This is because both threads are trying to
# access sys.stdout at the same time. This is known as a race condition.

# In order to prevent this from happening, we can use a lock.

import sys, threading
lock = threading.Lock() # create a lock object
for i in range(5):
    threading.Thread(target=lambda: sys.stdout.write(str(i))).start()
for i in range(5):
    threading.Thread(target=lambda: lock.acquire() or sys.stdout.write(str(i)) or lock
