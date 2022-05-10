import threading
threading.stack_size(2**27)
import sys

sys.setrecursionlimit(10**7)

thread = threading.Thread(target = calculate, args = ()) 
thread.start()

print("Thread started")
