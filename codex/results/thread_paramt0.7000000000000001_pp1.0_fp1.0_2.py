import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Start\n')).start()
print('Finish')

# Finish
# Start

# Note the order of the output. 
# The output is not what we expect it to be. 
# If we run this code, the output is not deterministic. 
# Sometimes the output will be:
# Start
# Finish
# but sometimes it will be:
# Finish
# Start

# This is because the print statement is executed by the main thread, 
# while the lambda is executed in the background. 
# The order in which the two threads are started is not guaranteed.

# This is a problem for multi-threaded programs.
# We have no way of knowing when a thread will start, 
# and what resources it will be using. 

# To fix this, we can use the print_lock.acquire() function to lock the print statement. 
# This allows only one thread to use the print statement at a time, 
# preventing race conditions.

# In the code below, we print using the print_lock rather than the built-in print function.
import sys
