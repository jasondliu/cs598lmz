import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello, world!\n")).start()

# it gets the job done, but it’s a bit hard to read.
# Here’s the same thing, but written in a more readable way:
import threading
import time

def thread_function(name):
    print("Thread {} starting".format(name))
    time.sleep(2)
    print("Thread {} finishing".format(name))

if __name__ == "__main__":
    x = threading.Thread(target=thread_function, args=(1,))
    y = threading.Thread(target=thread_function, args=(2,))
    z = threading.Thread(target=thread_function, args=(3,))
    x.start()
    y.start()
    z.start()
    print("Done!")

# threading.Thread is a class that we use to create a thread. 
# It takes two arguments: a function to run, and any arguments to pass to that function. 
# Then we call the start() method to start the thread.
