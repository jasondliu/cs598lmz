import threading
# Test threading daemonic mode by creating non-daemonic, waiting
# thread and then test whether it finishes. 

def done(*args):
    print("done")

def wait ():
   print("wait")

# create non-daemonic thread and wait 3 seconds, then exit
w = threading.Thread(name="wait", target=wait, daemon=False)

w.start()
time.sleep(3)
w.join() # wait for thread to exit

print("main thread exit")
