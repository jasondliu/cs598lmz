import threading
# Test threading daemon:
import threading
import time
def a():
    print 123
threading.Thread(target=a).setDaemon(True)
while True:
    print '123'
    time.sleep(1)

# %%{"gradable": true, "name": "Debugging: Warming up"}
# Use this cell to get familiar with the debugger.
# 
# Debug this function:
def f(x, y):
    a = x + 2
    b = y * x
    c = x - y
    print a, b, c
    return

z = f(3, 4)

# %%{"gradable": true, "name": "Debugging: Inserts and Watches"}
# Use this cell to get familiar with the debugger.
# 
# Debug this function:
def f(x, y):
    a = x + 2  # Set a breakpoint here, step over.
    b = y * x  # Run until this line, step over.
    c = x - y  # Set a breakpoint here, step over.
    print a, b, c 
