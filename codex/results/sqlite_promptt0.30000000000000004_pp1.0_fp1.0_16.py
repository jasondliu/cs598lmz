import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/home/pi/Desktop/test.db")

# Define the function to be called when the signal is received
def handler(signum, frame):
    print("Signal handler called with signal", signum)
    #raise IOError("Couldn't open device!")

# Register the signal handler
signal.signal(signal.SIGALRM, handler)

# Define a timeout for your function/method.
timeout = 5

# Set an alarm for 5 seconds
signal.alarm(timeout)

# Start the timer. Once 5 seconds are over, a SIGALRM signal is sent.
# Your signal handler gets executed and a KeyboardInterrupt is raised.
# If you are using signal.alarm in a non-main thread, the KeyboardInterrupt
# will be raised in the context of that non-main thread.

# If no timeout is needed, use signal.alarm(0) to disable the alarm.

# Define the function to be called when the signal is received
def handler(signum, frame):
    print("Signal handler called with signal", signum)
