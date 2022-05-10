import threading
threading.current_thread()

# Create two threads as follows
t1 = threading.Thread(target=task1, name='t1')
t2 = threading.Thread(target=task2, name='t2')

# Start running the threads
t1.start()
t2.start()

# Demonstrate that the main thread exited before the threads
print('Main thread is done!')

# Note the use of time.sleep() to allow the threads time to run.
# Importing time allows our program to sleep (i.e., pause) for a number of seconds (in this 
# case a value of 1).
# A real world application would use time.sleep() as a means to wait for a slow process to finish.
