import sys, threading

def run():
    print("Hello")

threading.Thread(target=run).start()

print("World")

# Output:
# World
# Hello

# This is because the print("World") statement is executed before the print("Hello") statement.
# The reason is that the print("World") statement is executed in the main thread, while the print("Hello") statement is executed in the newly created thread.
# The main thread is finished before the new thread is started.

# We can get the desired output by waiting for the thread to finish using the join() method.

import sys, threading

def run():
    print("Hello")

threading.Thread(target=run).start()

print("World")

