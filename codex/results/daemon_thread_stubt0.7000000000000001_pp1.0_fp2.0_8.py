import sys, threading

def run():
    print("Hello from new thread")

thread = threading.Thread(target=run)
thread.start()
print("Hello from main thread")

# NOTE: after running this code, you may not see the "Hello from new thread" message
#       that means that the main thread terminated before the other thread had a chance
#       to print

# NOTE: this code is a little bit different than the code in the book. The code in the
#       book is out-of-date, and not compatible with Python 3.x. The code above runs
#       fine on Python 3.x.
