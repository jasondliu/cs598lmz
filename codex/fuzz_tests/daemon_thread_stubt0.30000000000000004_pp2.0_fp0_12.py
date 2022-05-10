import sys, threading

def run():
    print("run")
    sys.exit(0)

threading.Thread(target=run).start()

print("Hello")

# Hello
# run

# This is because the thread starts and then immediately exits,
# so the main thread never gets a chance to print "Hello".
# To fix this, we can use the join() method to wait for the
# thread to finish.

import sys, threading

def run():
    print("run")
    sys.exit(0)

threading.Thread(target=run).start()

print("Hello")

# Hello
# run

# This is because the thread starts and then immediately exits,
# so the main thread never gets a chance to print "Hello".
# To fix this, we can use the join() method to wait for the
# thread to finish.

import sys, threading

def run():
    print("run")
    sys.exit(0)

threading.Thread(target=run).start()

print("Hello")

# Hello
# run

# This is because the thread
