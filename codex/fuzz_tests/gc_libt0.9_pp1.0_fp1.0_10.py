import gc, weakref
import threading, time

class C:
    pass

bar = weakref.finalize(C(), lambda x: print("garbage collected", x))
print("1:", bar)

# CAVEAT: There's no guarantee that collecting the object here will
# result in garbge collection; the object may be being held alive
# by a reference outside of the caller's control.  Also, a bug in
# the implementation could result in the object remaining alive long
# after this has run.
gc.collect()
print("2:", bar)

print("3:")
del bar
gc.collect() # should force finalization
print("4:")
time.sleep(0.1)
print("5:")

# no guarantee that will run finalizer soon in a multi-thread program
t = threading.Thread(target=lambda: print("6:", bar))
t.start()
t.join()
time.sleep(0.1)
