import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 2\n')).start()

# Threads normally run in parallel, but there is no guarantee of it
# One of the threads may run first, but there is no guarantee
# To fix this, we can use locks

import sys, threading
mutex = threading.Lock()
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 2\n')).start()

# This is still not perfect
# The threads may still run in parallel, but one of them will have to wait for the lock
# To fix this, we can use semaphores

import sys, threading
sema = threading.Semaphore(0)
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 1\n')).start()
