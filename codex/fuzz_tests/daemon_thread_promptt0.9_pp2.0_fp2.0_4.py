import threading
# Test threading daemon thread in action.
def B():
    print("Starts B")
    while True:
        time.sleep(2)
        print("B: still working")

d = threading.Thread(name='daemon', target=B)
d.setDaemon(True)
d.start()

d.join()  # This is the infinite loop for program to hang in.
print("join executed")

"""
Important:
In order to catch interruption from outside, use KeyboardInterrupt or Ctrl-C to stop the program.
This is an example of using the break to break from the infinite loop in the program.
"""

"""
Daemon threads vs non-daemon threads.
When the main thread exits, any outstanding non-daemon threads are cancelled. 
But when the main thread exits, any outstanding daemon threads are quietly ignored.
Duplicate the code above with additional arguments in the time.sleep() to see the effects.
"""
