import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello\n")).start()

print("World")

# Output:
# World
# Hello

# ----------------------------------------------------------------------------------------------------------------------

# Using a threading.Event
import sys, threading
event = threading.Event()

def hello():
    print("Hello")
    event.set()

threading.Thread(target=hello).start()

print("World")
event.wait()

# Output:
# World
# Hello

# ----------------------------------------------------------------------------------------------------------------------

# Using a threading.Condition
import sys, threading
condition = threading.Condition()

def hello():
    with condition:
        print("Hello")
        condition.notify()

threading.Thread(target=hello).start()

with condition:
    print("World")
    condition.wait()

# Output:
# World
# Hello

# ----------------------------------------------------------------------------------------------------------------------

# Using a threading.Semaphore
import sys, threading
semaphore = threading.Semaphore(0)

def hello():
    print("Hello
