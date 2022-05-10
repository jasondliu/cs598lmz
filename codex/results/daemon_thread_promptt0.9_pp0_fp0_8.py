import threading
# Test threading daemon vs non-daemon
# 0 <-> 1 | in seconds

# This has a daemon thread. It will die when the main thread died.
# |
# v
def f():
    while True:
        print(".");
        time.sleep(1)

t2=threading.Thread(target=f)
t2.setDaemon(True)
t2.start()
# ^
# |
# note that the thread does die when the main program exited.


# This does not.
# It will keep printing ".", even when the main thread died.
# |
# v
def g():
	while True:
		print("x")
		time.sleep(1)

t2=threading.Thread(target=g)
t2.start()
# ^
# |
# Note that the thread does *not* die when the main program exited.
