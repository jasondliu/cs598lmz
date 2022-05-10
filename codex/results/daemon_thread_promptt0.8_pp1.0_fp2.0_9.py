import threading
# Test threading daemon property:
#   If a daemonic thread blocks indefinitely at the join method of a non-daemonic thread,
#   the whole process hangs.
# In the test below, the daemonic thread shouldn't hang the whole process.

def worker():
    t = threading.currentThread()
    while getattr(t, "do_run", True): pass

t1 = threading.Thread(target=worker)
t1.start()

t2 = threading.Thread(target=worker)
t2.daemon = True
t2.start()

t1.join()
# The process should terminate.
# If it doesn't, the test failed.
