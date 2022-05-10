import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from Thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from Thread 2\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from Thread 3\n')).start()

# Threads share global memory space with the main program, but each thread has its own independent set of local variables.
# Local variables are not shared across threads.

# Locks
# Locks are a mechanism for enforcing mutual exclusion among threads that are competing for access to a shared resource.
# You create a lock by calling the threading.Lock() function.
# You can acquire a lock by calling its acquire() method, and you can release it by calling its release() method.
# If you try to release a lock that isn’t held or acquire a lock that is already held, your program will deadlock.
# Locks are useful for protecting access to a shared resource, such as a file or database.

# Semaphores
# Semaphores are a generalization of locks. Whereas a lock allows only one thread to acquire
