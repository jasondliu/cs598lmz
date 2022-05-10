import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello ")).start()
threading.Thread(target=lambda: sys.stdout.write("Python ")).start()
threading.Thread(target=lambda: sys.stdout.write("World!\n")).start()

# Python can also be used to create a single thread.
import time

def print_hello(thread_name):
    time.sleep(1)
    print("Hello from " + thread_name)

if __name__ == "__main__":
    print("Hello from the main thread!")
    print_hello("Thread #1")
    print("Goodbye from the main thread!")

# Take a look at the output of this program. Notice that even though the
# main thread is the first to print, the thread named "Thread #1" is the
# second to print. This is because the main thread creates a new thread,
# but then continues to execute while the new thread sleeps.

# Creating a thread in Python is done by extending the Thread class.
import threading

class MyThread(threading.Thread):
    def __
