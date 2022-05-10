import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello from threading\n")).start()
import time
time.sleep(1)
print("Hello from main thread")

# Hello from threading
# Hello from main thread

# This is the only way to get the actual thread id
import threading
threading.current_thread().ident

# The id is a number that is unique for each thread that is running.
# The id is not guaranteed to be the same from one run to the next.
# This is the only way to get the actual thread id
import threading
threading.current_thread().ident

# The id is a number that is unique for each thread that is running.
# The id is not guaranteed to be the same from one run to the next.

# Threads can communicate with each other.
# A thread can wait for another thread to finish by calling its join method.
# The following program starts a thread that counts to 10 and then exits.
# The main thread waits for the first thread to finish by calling its join method.
import threading

