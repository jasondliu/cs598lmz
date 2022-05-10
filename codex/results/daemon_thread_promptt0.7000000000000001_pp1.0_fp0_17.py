import threading
# Test threading daemon

def hello(name):
    print("Hello {}".format(name))
    time.sleep(1)
    print("world!")

# make a thread
thread = threading.Thread(target=hello, args=("haha",))
# set daemon
thread.setDaemon(True)
thread.start()
print("main thread out")

# main thread out
# Hello haha
# world!

# you can see, main thread didn't wait the sub thread finishing,
# that's because we set the sub thread as a daemon
# so when main thread exit, it will kill all sub thread daemon

# In production, you should set the sub thread as a daemon

# is_alive()
# is_alive() is to check if the thread is alive
# isAlive() need to use the Uppercase A, because
# it's a builtin function
# https://docs.python.org/3/library/threading.html#threading.Thread.is_alive

# join()
# join() is to wait the sub thread finishing
# https://docs.python.
