import sys, threading
threading.Thread(target=lambda: sys.stdout.write('1')).start()
sys.stdout.write('2')
# prints 21

# Data races
# A data race condition occurs when two or more threads access the same variable but at least one of the threads modifies it.
# In the example below
#  - Thread 1 acquires a lock on x
#  - Thread 2 then tries to acquire a lock on x, but has to wait.
#  - Thread 1 then modifies x and releases the lock.
#  - Thread 2 then acquires the lock and prints the value of x.
# So it's possible that we see the value 3 printed to the console.

# Solution 1:
# use a lock to prevent a data race condition from occurring when accessing x.
# In this case, we acquire the lock, modify x, and then release the lock.
# This means that only one thread can access x at a time.

# Solution 2:
# use the keyword global to specify that we want to modify the global value of x.
# This means that all threads will see the same value.
import threading
import time

x = 0

