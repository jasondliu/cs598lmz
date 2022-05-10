import threading
# Test threading daemonic

def dothread(threadnum, sleeptime):
    print("thread", threadnum, "before sleep", flush=True)
    time.sleep(sleeptime)
    print("thread", threadnum, "after sleep", flush=True)

for threadnum in range(10):
    th = threading.Thread(
        target=dothread, 
        args=(threadnum, 10+threadnum),
        daemon=True
        )
    th.start()
 
print("TEST END", flush=True)

# There is almost none output from this program, and it terminates almost immediately
# (small delay for default daemon threads TIME_JOIN)

# In the output, the part of threads before sleep is missing
# If the main thread ends, all daemon threads terminate, 
# and possibly before they even have time to start running !

# So do NOT rely on printar that are made inside a thread, 
# this is probably not going to give the output you expect


# From output, not all threads gets to run, they start as they can,
# and this changes
