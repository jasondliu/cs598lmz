import threading
# Test threading daemon
def wait(thread_id, name, x):
    print("\nI am %s (thread %s):" % (name, thread_id))
    time.sleep(x)
    print("%s finished waiting %s sec." % (name, x))
    return

t1 = threading.Thread(target=wait, args=(1, "thread 1", 4), name="t1")
t1.daemon = False
t1 = threading.Thread(target=wait, args=(2, "thread 2", 2), name="t2")
t2.daemon = False
t2 = threading.Thread(target=wait, args=(3, "thread 3", 1), name="t3")
t3.daemon = True
t1.start()
t2.start()
t3.start()
print("All thread started")
