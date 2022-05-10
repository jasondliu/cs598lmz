import threading
# Test threading daemon
def worker(n):
    print("%s started" % threading.current_thread().name)
    sleep(1)
    print("%s finished" % threading.current_thread().name)

print("%s started" % threading.current_thread().name)

for i in range(5):
    t = threading.Thread(target=worker, args=(i,), name="Thread %i" % i)
    t.daemon = True
    t.start()

print("%s finished" % threading.current_thread().name)

# Main thread finished before all other threads

# Main thread finished
# Main thread started
# Thread 0 started
# Thread 1 started
# Thread 2 started
# Thread 3 started
# Thread 4 started
# Thread 1 finished
# Thread 2 finished
# Thread 0 finished
# Thread 3 finished
# Thread 4 finished
