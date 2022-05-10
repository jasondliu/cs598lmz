import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

# 3
import threading
import time

def printit():
    threading.Timer(5.0, printit).start()
    print("Hello, World!")

printit()

# 4
import threading
import time

def printit():
    threading.Timer(5.0, printit).start()
    print("Hello, World!")

printit()

# 5
import threading
import time

def printit():
    threading.Timer(5.0, printit).start()
    print("Hello, World!")

printit()

# 6
import threading
import time

def printit():
    threading.Timer(5.0, printit).start()
    print("Hello, World!")

printit()

# 7
import threading
import time

def printit():
    threading.Timer(5.0, printit).start()
    print("Hello, World!")

printit()

# 8
import thread
